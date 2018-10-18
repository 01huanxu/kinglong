# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hmi_car_device_pb2 as hmi__car__device__pb2
import hmi_collect_data_pb2 as hmi__collect__data__pb2
import hmi_common_pb2 as hmi__common__pb2
import hmi_driving_control_pb2 as hmi__driving__control__pb2
import hmi_fetch_msg_pb2 as hmi__fetch__msg__pb2
import hmi_hudinfo_pb2 as hmi__hudinfo__pb2
import hmi_launch_pb2 as hmi__launch__pb2
import hmi_localization_init_pb2 as hmi__localization__init__pb2
import hmi_map_info_pb2 as hmi__map__info__pb2
import hmi_ota_pb2 as hmi__ota__pb2
import hmi_routing_pb2 as hmi__routing__pb2
import hmi_system_control_pb2 as hmi__system__control__pb2
import hmi_world_pb2 as hmi__world__pb2
import ota_pb2 as ota__pb2


class HMIGrpcServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FetchSectionMsg = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/FetchSectionMsg',
        request_serializer=hmi__fetch__msg__pb2.FetchKeys.SerializeToString,
        response_deserializer=hmi__fetch__msg__pb2.WorldPackage.FromString,
        )
    self.FetchMapElement = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/FetchMapElement',
        request_serializer=hmi__map__info__pb2.MapFileRequest.SerializeToString,
        response_deserializer=hmi__map__info__pb2.MapFileResponse.FromString,
        )
    self.FetchMapVersion = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/FetchMapVersion',
        request_serializer=hmi__fetch__msg__pb2.MapVersionRequest.SerializeToString,
        response_deserializer=hmi__fetch__msg__pb2.MapVersionResponse.FromString,
        )
    self.FetchSafeCheckResult = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/FetchSafeCheckResult',
        request_serializer=hmi__fetch__msg__pb2.SafeCheckRequest.SerializeToString,
        response_deserializer=hmi__world__pb2.SafeCheckResponse.FromString,
        )
    self.ShutdownSystem = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/ShutdownSystem',
        request_serializer=hmi__system__control__pb2.SystemControlRequest.SerializeToString,
        response_deserializer=hmi__system__control__pb2.SystemControlResponse.FromString,
        )
    self.TransferSystemControl = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/TransferSystemControl',
        request_serializer=hmi__system__control__pb2.TransferControlRequest.SerializeToString,
        response_deserializer=hmi__system__control__pb2.TransferControlResponse.FromString,
        )
    self.PreRouting = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/PreRouting',
        request_serializer=hmi__routing__pb2.RoutingRequest.SerializeToString,
        response_deserializer=hmi__routing__pb2.RoutingResponse.FromString,
        )
    self.StartRouting = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/StartRouting',
        request_serializer=hmi__routing__pb2.RoutingRequest.SerializeToString,
        response_deserializer=hmi__routing__pb2.RoutingResponse.FromString,
        )
    self.Launch = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/Launch',
        request_serializer=hmi__launch__pb2.LaunchRequest.SerializeToString,
        response_deserializer=hmi__launch__pb2.LaunchResponse.FromString,
        )
    self.Disengage = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/Disengage',
        request_serializer=hmi__launch__pb2.DisengageRequest.SerializeToString,
        response_deserializer=hmi__launch__pb2.DisengageResponse.FromString,
        )
    self.StopAndGo = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/StopAndGo',
        request_serializer=hmi__driving__control__pb2.SwitchCarStateRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.CheckPositionStatus = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/CheckPositionStatus',
        request_serializer=hmi__driving__control__pb2.PositionStatusRequest.SerializeToString,
        response_deserializer=hmi__driving__control__pb2.PositionStatusResponse.FromString,
        )
    self.CheckParkingRelation = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/CheckParkingRelation',
        request_serializer=hmi__driving__control__pb2.ParkingRelationRequest.SerializeToString,
        response_deserializer=hmi__driving__control__pb2.ParkingRelationResponse.FromString,
        )
    self.AutoParking = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/AutoParking',
        request_serializer=hmi__driving__control__pb2.AutoParkingRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.AutoOutGarage = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/AutoOutGarage',
        request_serializer=hmi__driving__control__pb2.AutoOutGarageRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.Intervene = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/Intervene',
        request_serializer=hmi__driving__control__pb2.InterveneRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.DisengageTypeFeedback = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/DisengageTypeFeedback',
        request_serializer=hmi__driving__control__pb2.DisengageTypeContent.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.SwitchDoor = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/SwitchDoor',
        request_serializer=hmi__car__device__pb2.DeciveControlRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.SwitchHeadLights = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/SwitchHeadLights',
        request_serializer=hmi__car__device__pb2.DeciveControlRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.SwitchFrontLamp = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/SwitchFrontLamp',
        request_serializer=hmi__car__device__pb2.DeciveControlRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.SwitchEmergencyLamp = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/SwitchEmergencyLamp',
        request_serializer=hmi__car__device__pb2.DeciveControlRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.SwitchCourtesyLamp = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/SwitchCourtesyLamp',
        request_serializer=hmi__car__device__pb2.DeciveControlRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.NotiAirCondition = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/NotiAirCondition',
        request_serializer=hmi__car__device__pb2.AirConditionRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.TriggerAlarmHorn = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/TriggerAlarmHorn',
        request_serializer=hmi__car__device__pb2.TriggerRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.TriggerEmergencyStop = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/TriggerEmergencyStop',
        request_serializer=hmi__car__device__pb2.TriggerRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.SetHudInfo = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/SetHudInfo',
        request_serializer=hmi__hudinfo__pb2.HudInfo.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.NotiOTAClient = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/NotiOTAClient',
        request_serializer=hmi__ota__pb2.OtaRequest.SerializeToString,
        response_deserializer=hmi__ota__pb2.OtaResponse.FromString,
        )
    self.FetchCollectDataMsg = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/FetchCollectDataMsg',
        request_serializer=hmi__collect__data__pb2.FetchCollectDataKey.SerializeToString,
        response_deserializer=hmi__collect__data__pb2.FetchCollectDataPackage.FromString,
        )
    self.NotiWorkingState = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/NotiWorkingState',
        request_serializer=hmi__collect__data__pb2.WorkStateRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.NotiDataCheck = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/NotiDataCheck',
        request_serializer=hmi__collect__data__pb2.DataCheckRequest.SerializeToString,
        response_deserializer=hmi__collect__data__pb2.DataCheckResult.FromString,
        )
    self.NotiHeartBeat = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/NotiHeartBeat',
        request_serializer=hmi__world__pb2.HeartBeatType.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.SwitchCollectMode = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/SwitchCollectMode',
        request_serializer=hmi__collect__data__pb2.CollectingStateRequest.SerializeToString,
        response_deserializer=hmi__common__pb2.StatusResponse.FromString,
        )
    self.FetchPreProcTaskStatus = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/FetchPreProcTaskStatus',
        request_serializer=hmi__fetch__msg__pb2.FetchPreProcTaskRequest.SerializeToString,
        response_deserializer=hmi__fetch__msg__pb2.PreProcTaskResult.FromString,
        )
    self.CheckCalibrationValidity = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/CheckCalibrationValidity',
        request_serializer=hmi__world__pb2.CalibrationValidityRequest.SerializeToString,
        response_deserializer=hmi__world__pb2.CalibrationValidityResponse.FromString,
        )
    self.StreamOtaToHmi = channel.stream_stream(
        '/adu.hmi.HMIGrpcService/StreamOtaToHmi',
        request_serializer=ota__pb2.OtaRequest.SerializeToString,
        response_deserializer=ota__pb2.OtaResponse.FromString,
        )
    self.StreamHmiToOta = channel.stream_stream(
        '/adu.hmi.HMIGrpcService/StreamHmiToOta',
        request_serializer=ota__pb2.OtaResponse.SerializeToString,
        response_deserializer=ota__pb2.OtaRequest.FromString,
        )
    self.NotiLocalizationInitPose = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/NotiLocalizationInitPose',
        request_serializer=hmi__localization__init__pb2.PositionAndHeading.SerializeToString,
        response_deserializer=hmi__localization__init__pb2.LocalInitRes.FromString,
        )
    self.MoveLogSync = channel.unary_unary(
        '/adu.hmi.HMIGrpcService/MoveLogSync',
        request_serializer=hmi__system__control__pb2.SystemControlRequest.SerializeToString,
        response_deserializer=hmi__system__control__pb2.SystemControlResponse.FromString,
        )


class HMIGrpcServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def FetchSectionMsg(self, request, context):
    """Fetch-API
    fetch basic message package
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchMapElement(self, request, context):
    """fetch hdmap for display
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchMapVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchSafeCheckResult(self, request, context):
    """fetch safety check result for once
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShutdownSystem(self, request, context):
    """Control-APIs
    system check & control
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransferSystemControl(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PreRouting(self, request, context):
    """routing control
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartRouting(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Launch(self, request, context):
    """driving control
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Disengage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopAndGo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckPositionStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckParkingRelation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AutoParking(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AutoOutGarage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Intervene(self, request, context):
    """driving intervene
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DisengageTypeFeedback(self, request, context):
    """disengage feedback
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SwitchDoor(self, request, context):
    """car device control
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SwitchHeadLights(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SwitchFrontLamp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SwitchEmergencyLamp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SwitchCourtesyLamp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotiAirCondition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TriggerAlarmHorn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TriggerEmergencyStop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetHudInfo(self, request, context):
    """set info from panel 2 hud
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotiOTAClient(self, request, context):
    """ota request from panel app
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchCollectDataMsg(self, request, context):
    """collection mode
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotiWorkingState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotiDataCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotiHeartBeat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SwitchCollectMode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchPreProcTaskStatus(self, request, context):
    """preprocess mode
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckCalibrationValidity(self, request, context):
    """calibration validity
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamOtaToHmi(self, request_iterator, context):
    """ota info transfer 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamHmiToOta(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NotiLocalizationInitPose(self, request, context):
    """noti assist localization init pose
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MoveLogSync(self, request, context):
    """move log
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HMIGrpcServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FetchSectionMsg': grpc.unary_unary_rpc_method_handler(
          servicer.FetchSectionMsg,
          request_deserializer=hmi__fetch__msg__pb2.FetchKeys.FromString,
          response_serializer=hmi__fetch__msg__pb2.WorldPackage.SerializeToString,
      ),
      'FetchMapElement': grpc.unary_unary_rpc_method_handler(
          servicer.FetchMapElement,
          request_deserializer=hmi__map__info__pb2.MapFileRequest.FromString,
          response_serializer=hmi__map__info__pb2.MapFileResponse.SerializeToString,
      ),
      'FetchMapVersion': grpc.unary_unary_rpc_method_handler(
          servicer.FetchMapVersion,
          request_deserializer=hmi__fetch__msg__pb2.MapVersionRequest.FromString,
          response_serializer=hmi__fetch__msg__pb2.MapVersionResponse.SerializeToString,
      ),
      'FetchSafeCheckResult': grpc.unary_unary_rpc_method_handler(
          servicer.FetchSafeCheckResult,
          request_deserializer=hmi__fetch__msg__pb2.SafeCheckRequest.FromString,
          response_serializer=hmi__world__pb2.SafeCheckResponse.SerializeToString,
      ),
      'ShutdownSystem': grpc.unary_unary_rpc_method_handler(
          servicer.ShutdownSystem,
          request_deserializer=hmi__system__control__pb2.SystemControlRequest.FromString,
          response_serializer=hmi__system__control__pb2.SystemControlResponse.SerializeToString,
      ),
      'TransferSystemControl': grpc.unary_unary_rpc_method_handler(
          servicer.TransferSystemControl,
          request_deserializer=hmi__system__control__pb2.TransferControlRequest.FromString,
          response_serializer=hmi__system__control__pb2.TransferControlResponse.SerializeToString,
      ),
      'PreRouting': grpc.unary_unary_rpc_method_handler(
          servicer.PreRouting,
          request_deserializer=hmi__routing__pb2.RoutingRequest.FromString,
          response_serializer=hmi__routing__pb2.RoutingResponse.SerializeToString,
      ),
      'StartRouting': grpc.unary_unary_rpc_method_handler(
          servicer.StartRouting,
          request_deserializer=hmi__routing__pb2.RoutingRequest.FromString,
          response_serializer=hmi__routing__pb2.RoutingResponse.SerializeToString,
      ),
      'Launch': grpc.unary_unary_rpc_method_handler(
          servicer.Launch,
          request_deserializer=hmi__launch__pb2.LaunchRequest.FromString,
          response_serializer=hmi__launch__pb2.LaunchResponse.SerializeToString,
      ),
      'Disengage': grpc.unary_unary_rpc_method_handler(
          servicer.Disengage,
          request_deserializer=hmi__launch__pb2.DisengageRequest.FromString,
          response_serializer=hmi__launch__pb2.DisengageResponse.SerializeToString,
      ),
      'StopAndGo': grpc.unary_unary_rpc_method_handler(
          servicer.StopAndGo,
          request_deserializer=hmi__driving__control__pb2.SwitchCarStateRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'CheckPositionStatus': grpc.unary_unary_rpc_method_handler(
          servicer.CheckPositionStatus,
          request_deserializer=hmi__driving__control__pb2.PositionStatusRequest.FromString,
          response_serializer=hmi__driving__control__pb2.PositionStatusResponse.SerializeToString,
      ),
      'CheckParkingRelation': grpc.unary_unary_rpc_method_handler(
          servicer.CheckParkingRelation,
          request_deserializer=hmi__driving__control__pb2.ParkingRelationRequest.FromString,
          response_serializer=hmi__driving__control__pb2.ParkingRelationResponse.SerializeToString,
      ),
      'AutoParking': grpc.unary_unary_rpc_method_handler(
          servicer.AutoParking,
          request_deserializer=hmi__driving__control__pb2.AutoParkingRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'AutoOutGarage': grpc.unary_unary_rpc_method_handler(
          servicer.AutoOutGarage,
          request_deserializer=hmi__driving__control__pb2.AutoOutGarageRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'Intervene': grpc.unary_unary_rpc_method_handler(
          servicer.Intervene,
          request_deserializer=hmi__driving__control__pb2.InterveneRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'DisengageTypeFeedback': grpc.unary_unary_rpc_method_handler(
          servicer.DisengageTypeFeedback,
          request_deserializer=hmi__driving__control__pb2.DisengageTypeContent.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'SwitchDoor': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchDoor,
          request_deserializer=hmi__car__device__pb2.DeciveControlRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'SwitchHeadLights': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchHeadLights,
          request_deserializer=hmi__car__device__pb2.DeciveControlRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'SwitchFrontLamp': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchFrontLamp,
          request_deserializer=hmi__car__device__pb2.DeciveControlRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'SwitchEmergencyLamp': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchEmergencyLamp,
          request_deserializer=hmi__car__device__pb2.DeciveControlRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'SwitchCourtesyLamp': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchCourtesyLamp,
          request_deserializer=hmi__car__device__pb2.DeciveControlRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'NotiAirCondition': grpc.unary_unary_rpc_method_handler(
          servicer.NotiAirCondition,
          request_deserializer=hmi__car__device__pb2.AirConditionRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'TriggerAlarmHorn': grpc.unary_unary_rpc_method_handler(
          servicer.TriggerAlarmHorn,
          request_deserializer=hmi__car__device__pb2.TriggerRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'TriggerEmergencyStop': grpc.unary_unary_rpc_method_handler(
          servicer.TriggerEmergencyStop,
          request_deserializer=hmi__car__device__pb2.TriggerRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'SetHudInfo': grpc.unary_unary_rpc_method_handler(
          servicer.SetHudInfo,
          request_deserializer=hmi__hudinfo__pb2.HudInfo.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'NotiOTAClient': grpc.unary_unary_rpc_method_handler(
          servicer.NotiOTAClient,
          request_deserializer=hmi__ota__pb2.OtaRequest.FromString,
          response_serializer=hmi__ota__pb2.OtaResponse.SerializeToString,
      ),
      'FetchCollectDataMsg': grpc.unary_unary_rpc_method_handler(
          servicer.FetchCollectDataMsg,
          request_deserializer=hmi__collect__data__pb2.FetchCollectDataKey.FromString,
          response_serializer=hmi__collect__data__pb2.FetchCollectDataPackage.SerializeToString,
      ),
      'NotiWorkingState': grpc.unary_unary_rpc_method_handler(
          servicer.NotiWorkingState,
          request_deserializer=hmi__collect__data__pb2.WorkStateRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'NotiDataCheck': grpc.unary_unary_rpc_method_handler(
          servicer.NotiDataCheck,
          request_deserializer=hmi__collect__data__pb2.DataCheckRequest.FromString,
          response_serializer=hmi__collect__data__pb2.DataCheckResult.SerializeToString,
      ),
      'NotiHeartBeat': grpc.unary_unary_rpc_method_handler(
          servicer.NotiHeartBeat,
          request_deserializer=hmi__world__pb2.HeartBeatType.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'SwitchCollectMode': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchCollectMode,
          request_deserializer=hmi__collect__data__pb2.CollectingStateRequest.FromString,
          response_serializer=hmi__common__pb2.StatusResponse.SerializeToString,
      ),
      'FetchPreProcTaskStatus': grpc.unary_unary_rpc_method_handler(
          servicer.FetchPreProcTaskStatus,
          request_deserializer=hmi__fetch__msg__pb2.FetchPreProcTaskRequest.FromString,
          response_serializer=hmi__fetch__msg__pb2.PreProcTaskResult.SerializeToString,
      ),
      'CheckCalibrationValidity': grpc.unary_unary_rpc_method_handler(
          servicer.CheckCalibrationValidity,
          request_deserializer=hmi__world__pb2.CalibrationValidityRequest.FromString,
          response_serializer=hmi__world__pb2.CalibrationValidityResponse.SerializeToString,
      ),
      'StreamOtaToHmi': grpc.stream_stream_rpc_method_handler(
          servicer.StreamOtaToHmi,
          request_deserializer=ota__pb2.OtaRequest.FromString,
          response_serializer=ota__pb2.OtaResponse.SerializeToString,
      ),
      'StreamHmiToOta': grpc.stream_stream_rpc_method_handler(
          servicer.StreamHmiToOta,
          request_deserializer=ota__pb2.OtaResponse.FromString,
          response_serializer=ota__pb2.OtaRequest.SerializeToString,
      ),
      'NotiLocalizationInitPose': grpc.unary_unary_rpc_method_handler(
          servicer.NotiLocalizationInitPose,
          request_deserializer=hmi__localization__init__pb2.PositionAndHeading.FromString,
          response_serializer=hmi__localization__init__pb2.LocalInitRes.SerializeToString,
      ),
      'MoveLogSync': grpc.unary_unary_rpc_method_handler(
          servicer.MoveLogSync,
          request_deserializer=hmi__system__control__pb2.SystemControlRequest.FromString,
          response_serializer=hmi__system__control__pb2.SystemControlResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.hmi.HMIGrpcService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
