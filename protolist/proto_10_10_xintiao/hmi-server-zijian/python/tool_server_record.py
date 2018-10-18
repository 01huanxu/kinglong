import cybertron
import re
import yaml
import xlog
import os
import sys

def save_channels_for_record(record):
    bag = cybertron.bag.Bag(record)
    temp_record = record + ".new"
    new_bag = cybertron.bag.Bag(temp_record, True)

    record_info = yaml.load(bag.get_yaml_info())
    xlog.info('record yaml info: %s' % record_info)

    with open('channel_name.yaml') as f:
        cont = f.read()

    channel_info = yaml.load(cont)
    channel_list = channel_info['ChannelNameListAll']
    xlog.info('channel yaml info: %s' % channel_list)


    topics = map(lambda x: x['topic'], record_info['topics'])
    xlog.info('topics: %s' % topics)

    remained_topics = []
    for channel in channel_list:
        for topic in topics:
            if re.match(channel, topic) is not None:
                print "keep:" + str(topic)
                xlog.info('keep topic: %s' % topic)
                remained_topics.append(channel)    
            else:
                # print "remove:" + str(topic)
                xlog.info('remove topic: %s' % topic)
    xlog.info('remained topics: %s' % remained_topics)

    while(len(remained_topics)!=0):
        remained_topic = []
        remained_topic.append(remained_topics.pop())
        print "pop msg:" + str(remained_topic)
        msg_num = 0
        bag = cybertron.bag.Bag(record)
        for topic, msg, msgtype, timestamp in bag.read_messages(remained_topic):
            print topic
            new_bag.write(topic, msg, msgtype, timestamp)
            msg_num = msg_num + 1
            if(msg_num > 1):
                break
        xlog.info('msg_num: %s' % str(msg_num))

    new_bag.set_snapshot(bag.get_snapshot())

    bag.close()
    new_bag.close()

    # os.remove(record)
    # os.rename(temp_record, record)

def remove_channels_for_task(task, channels):
    xlog.info('remove channels for task %s' % task)
    for root, dirnames, filenames in os.walk(task + '/cyberecord'):
        # print root, dirnames, filenames
        for filename in filenames:
            path = os.path.join(root, filename)
            if path.endswith('.record'):
                xlog.info('remove channels for record %s' % path)
                remove_channels_for_record(str(path), channels)

def read_topic_test():
    bag = cybertron.bag.Bag('/home/caros/record/dasha_running_20180824.record')
    remained_topic_1 = ['/pnc/decision', '/pnc/carstatus']
    remained_topic_2 = ['/pnc/carstatus']
    for topic, msg, msgtype, timestamp in bag.read_messages(remained_topic_1):
        print topic
        print "##"
    # for topic, msg, msgtype, timestamp in bag.read_messages(remained_topic_2):
    #     print topic
    #     break
    bag.close()

if __name__ == '__main__':
    xlog.init('record_channel_tool')
    save_channels_for_record('/home/caros/record/dasha_running_20180824.record')
    # read_topic_test()