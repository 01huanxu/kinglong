import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../proto')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../python')

import unittest
import grpc
import time
import yaml
import thread
import conf_loader
import hmi_error_code_pb2
import launcher_grpc_api_pb2_grpc
import launcher_pb2


channel = grpc.insecure_channel('127.0.0.1:8090')
stub = launcher_grpc_api_pb2_grpc.LauncherServiceStub(channel)


class TestLauncher(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLauncher, self).__init__(*args, **kwargs)
        cf = conf_loader.ConfLoader("conf/hmi_launcher.test.yml")
        self._test_worker = cf.prms['workers'][0]['name']

    def get_worker_status(self, name):
        res = stub.GetWorkers(launcher_pb2.GetWorkersRequest(
            client_id='hmi-panel', worker_names=[name]))
        # print res
        self.assertTrue(res.code == hmi_error_code_pb2.OK, res)
        return res.workers[0].status

    def start_worker(self, name, client_id, wait=False, wait_timeout=0):
        req = launcher_pb2.ControlWorkersRequest(client_id=client_id)
        cmd = req.requests.add()
        cmd.worker_name = self._test_worker
        cmd.command = 'start'
        req.wait = wait
        req.wait_timeout = wait_timeout
        res = stub.ControlWorkers(req)
        # print res
        self.assertTrue(res.code == hmi_error_code_pb2.OK, res)
        return res

    def stop_worker(self, name, client_id):
        req = launcher_pb2.ControlWorkersRequest(client_id=client_id)
        cmd = req.requests.add()
        cmd.worker_name = name
        cmd.command = 'stop'
        res = stub.ControlWorkers(req)
        # print res
        self.assertTrue(res.code == hmi_error_code_pb2.OK, res)
        self.assertTrue(res.responses[0].code == hmi_error_code_pb2.OK, res)
        return res

    def check_timeout(self, assert_func, timeout_s):
        counter = 0
        while assert_func():
            time.sleep(0.1)
            counter += 1
        self.assertTrue(counter < timeout_s * 10, float(counter) / 10)

    def test_control_workers(self):
        print('')
        print('ensure worker stopped...')
        if self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED:
            self.stop_worker(self._test_worker, 'hmi-hud')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED, 1)

        print('start worker...')
        self.start_worker(self._test_worker, 'hmi-hud')

        print('wait worker initialize...')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) == launcher_pb2.NOT_STARTED, 2)

        print('wait worker start...')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) == launcher_pb2.INITIALIZING, 5)

        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.RUNNING)

        time.sleep(2)
        print('stop worker...')
        self.stop_worker(self._test_worker, 'hmi-hud')

        time.sleep(2)
        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.NOT_STARTED)

    def test_start_counter(self):
        print('')
        print('ensure worker stopped...')
        if self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED:
            self.stop_worker(self._test_worker, 'hmi-hud')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED, 1)

        print('start worker...')
        self.start_worker(self._test_worker, 'hmi-hud')

        print('wait worker initialize...')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) == launcher_pb2.NOT_STARTED, 1)

        print('wait worker start...')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) == launcher_pb2.INITIALIZING, 5)

        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.RUNNING)

        print('start worker twice...')
        self.start_worker(self._test_worker, 'hmi-panel')

        time.sleep(2)
        print('stop worker...')
        self.stop_worker(self._test_worker, 'hmi-hud')

        time.sleep(2)
        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.RUNNING)

        time.sleep(2)
        print('stop worker twice...')
        self.stop_worker(self._test_worker, 'hmi-panel')

        time.sleep(2)
        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.NOT_STARTED)

    def test_script(self):
        print('')
        print('start script...')
        req = launcher_pb2.ControlWorkersRequest(client_id='hmi-hud')
        cmd = req.requests.add()
        cmd.worker_name = 'script'
        cmd.command = 'sleep'
        res = stub.ControlWorkers(req)
        # print res
        self.assertTrue(res.code == hmi_error_code_pb2.OK, res)

        print('wait script start...')
        counter1 = 0
        while self.get_worker_status('script') == launcher_pb2.NOT_STARTED:
            time.sleep(0.1)
            counter1 += 1

        print('wait script stop...')
        counter2 = 23
        while self.get_worker_status('script') == launcher_pb2.RUNNING:
            time.sleep(1)
            counter2 -= 1
            if counter2 <= 0:
                break

        print('start counter: %d, stop counter: %d' % (counter1, counter2))
        self.assertTrue(self.get_worker_status(
            'script') == launcher_pb2.NOT_STARTED)

    def test_wait(self):
        print('')
        print('ensure worker stopped...')
        if self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED:
            self.stop_worker(self._test_worker, 'hmi-hud')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED, 1)

        print('start worker...')
        res = self.start_worker(self._test_worker, 'hmi-hud', True)
        print('ensure worker info...')
        self.assertTrue(res.responses[0].info.status == launcher_pb2.RUNNING)
        self.assertTrue(res.responses[0].info.HasField('ip'))
        self.assertTrue(res.responses[0].info.HasField('port'))

        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.RUNNING)

        print('stop worker...')
        self.stop_worker(self._test_worker, 'hmi-hud')

        time.sleep(2)
        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.NOT_STARTED)

    def test_wait_timeout(self):
        print('')
        print('ensure worker stopped...')
        if self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED:
            self.stop_worker(self._test_worker, 'hmi-hud')
        self.check_timeout(lambda: self.get_worker_status(self._test_worker) != launcher_pb2.NOT_STARTED, 1)

        print('start worker...')
        res = self.start_worker(self._test_worker, 'hmi-hud', True, 1)
        print('ensure worker info...')
        self.assertTrue(res.responses[0].info.status != launcher_pb2.RUNNING)

        print('stop worker...')
        self.stop_worker(self._test_worker, 'hmi-hud')

        time.sleep(2)
        self.assertTrue(self.get_worker_status(
            self._test_worker) == launcher_pb2.NOT_STARTED)


if __name__ == '__main__':
    cybertron_path = os.environ['CYBERTRON_PATH']
    cmd = cybertron_path + '/bin/hmi_server --flagfile=' \
        + os.path.abspath(os.path.dirname(__file__)) + '/conf/hmi_server.conf --hmi_launcher_config=' \
        + os.path.abspath(os.path.dirname(__file__)) + \
        '/conf/hmi_launcher.test.yml > /dev/null 2>&1'
    thread.start_new_thread(os.system, (cmd,))
    time.sleep(5)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestLauncher)
    unittest.TextTestRunner(verbosity=2).run(suite)

    os.system('pkill -9 hmi_server')
