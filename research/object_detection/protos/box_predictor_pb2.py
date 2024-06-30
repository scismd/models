# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/box_predictor.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'object_detection/protos/box_predictor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import hyperparams_pb2 as object__detection_dot_protos_dot_hyperparams__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+object_detection/protos/box_predictor.proto\x12\x17object_detection.protos\x1a)object_detection/protos/hyperparams.proto\"\x90\x03\n\x0c\x42oxPredictor\x12Y\n\x1b\x63onvolutional_box_predictor\x18\x01 \x01(\x0b\x32\x32.object_detection.protos.ConvolutionalBoxPredictorH\x00\x12P\n\x17mask_rcnn_box_predictor\x18\x02 \x01(\x0b\x32-.object_detection.protos.MaskRCNNBoxPredictorH\x00\x12G\n\x12rfcn_box_predictor\x18\x03 \x01(\x0b\x32).object_detection.protos.RfcnBoxPredictorH\x00\x12s\n)weight_shared_convolutional_box_predictor\x18\x04 \x01(\x0b\x32>.object_detection.protos.WeightSharedConvolutionalBoxPredictorH\x00\x42\x15\n\x13\x62ox_predictor_oneof\"\xaf\x04\n\x19\x43onvolutionalBoxPredictor\x12>\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\x14\n\tmin_depth\x18\x02 \x01(\x05:\x01\x30\x12\x14\n\tmax_depth\x18\x03 \x01(\x05:\x01\x30\x12&\n\x1bnum_layers_before_predictor\x18\x04 \x01(\x05:\x01\x30\x12\x19\n\x0buse_dropout\x18\x05 \x01(\x08:\x04true\x12%\n\x18\x64ropout_keep_probability\x18\x06 \x01(\x02:\x03\x30.8\x12\x16\n\x0bkernel_size\x18\x07 \x01(\x05:\x01\x31\x12\x18\n\rbox_code_size\x18\x08 \x01(\x05:\x01\x34\x12&\n\x17\x61pply_sigmoid_to_scores\x18\t \x01(\x08:\x05\x66\x61lse\x12%\n\x1a\x63lass_prediction_bias_init\x18\n \x01(\x02:\x01\x30\x12\x1c\n\ruse_depthwise\x18\x0b \x01(\x08:\x05\x66\x61lse\x12j\n\x18\x62ox_encodings_clip_range\x18\x0c \x01(\x0b\x32H.object_detection.protos.ConvolutionalBoxPredictor.BoxEncodingsClipRange\x1a\x31\n\x15\x42oxEncodingsClipRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"\xad\x06\n%WeightSharedConvolutionalBoxPredictor\x12>\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12.\n\x1f\x61pply_conv_hyperparams_to_heads\x18\x13 \x01(\x08:\x05\x66\x61lse\x12/\n apply_conv_hyperparams_pointwise\x18\x14 \x01(\x08:\x05\x66\x61lse\x12&\n\x1bnum_layers_before_predictor\x18\x04 \x01(\x05:\x01\x30\x12\x10\n\x05\x64\x65pth\x18\x02 \x01(\x05:\x01\x30\x12\x16\n\x0bkernel_size\x18\x07 \x01(\x05:\x01\x33\x12\x18\n\rbox_code_size\x18\x08 \x01(\x05:\x01\x34\x12%\n\x1a\x63lass_prediction_bias_init\x18\n \x01(\x02:\x01\x30\x12\x1a\n\x0buse_dropout\x18\x0b \x01(\x08:\x05\x66\x61lse\x12%\n\x18\x64ropout_keep_probability\x18\x0c \x01(\x02:\x03\x30.8\x12%\n\x16share_prediction_tower\x18\r \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ruse_depthwise\x18\x0e \x01(\x08:\x05\x66\x61lse\x12p\n\x0fscore_converter\x18\x10 \x01(\x0e\x32M.object_detection.protos.WeightSharedConvolutionalBoxPredictor.ScoreConverter:\x08IDENTITY\x12v\n\x18\x62ox_encodings_clip_range\x18\x11 \x01(\x0b\x32T.object_detection.protos.WeightSharedConvolutionalBoxPredictor.BoxEncodingsClipRange\x1a\x31\n\x15\x42oxEncodingsClipRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"+\n\x0eScoreConverter\x12\x0c\n\x08IDENTITY\x10\x00\x12\x0b\n\x07SIGMOID\x10\x01\"\xbf\x04\n\x14MaskRCNNBoxPredictor\x12<\n\x0e\x66\x63_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\x1a\n\x0buse_dropout\x18\x02 \x01(\x08:\x05\x66\x61lse\x12%\n\x18\x64ropout_keep_probability\x18\x03 \x01(\x02:\x03\x30.5\x12\x18\n\rbox_code_size\x18\x04 \x01(\x05:\x01\x34\x12>\n\x10\x63onv_hyperparams\x18\x05 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12%\n\x16predict_instance_masks\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\'\n\x1amask_prediction_conv_depth\x18\x07 \x01(\x05:\x03\x32\x35\x36\x12 \n\x11predict_keypoints\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x0bmask_height\x18\t \x01(\x05:\x02\x31\x35\x12\x16\n\nmask_width\x18\n \x01(\x05:\x02\x31\x35\x12*\n\x1fmask_prediction_num_conv_layers\x18\x0b \x01(\x05:\x01\x32\x12\'\n\x18masks_are_class_agnostic\x18\x0c \x01(\x08:\x05\x66\x61lse\x12\'\n\x18share_box_across_classes\x18\r \x01(\x08:\x05\x66\x61lse\x12+\n\x1c\x63onvolve_then_upsample_masks\x18\x0e \x01(\x08:\x05\x66\x61lse\"\xf9\x01\n\x10RfcnBoxPredictor\x12>\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\"\n\x17num_spatial_bins_height\x18\x02 \x01(\x05:\x01\x33\x12!\n\x16num_spatial_bins_width\x18\x03 \x01(\x05:\x01\x33\x12\x13\n\x05\x64\x65pth\x18\x04 \x01(\x05:\x04\x31\x30\x32\x34\x12\x18\n\rbox_code_size\x18\x05 \x01(\x05:\x01\x34\x12\x17\n\x0b\x63rop_height\x18\x06 \x01(\x05:\x02\x31\x32\x12\x16\n\ncrop_width\x18\x07 \x01(\x05:\x02\x31\x32')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.box_predictor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOXPREDICTOR']._serialized_start=116
  _globals['_BOXPREDICTOR']._serialized_end=516
  _globals['_CONVOLUTIONALBOXPREDICTOR']._serialized_start=519
  _globals['_CONVOLUTIONALBOXPREDICTOR']._serialized_end=1078
  _globals['_CONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE']._serialized_start=1029
  _globals['_CONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE']._serialized_end=1078
  _globals['_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR']._serialized_start=1081
  _globals['_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR']._serialized_end=1894
  _globals['_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE']._serialized_start=1029
  _globals['_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_BOXENCODINGSCLIPRANGE']._serialized_end=1078
  _globals['_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_SCORECONVERTER']._serialized_start=1851
  _globals['_WEIGHTSHAREDCONVOLUTIONALBOXPREDICTOR_SCORECONVERTER']._serialized_end=1894
  _globals['_MASKRCNNBOXPREDICTOR']._serialized_start=1897
  _globals['_MASKRCNNBOXPREDICTOR']._serialized_end=2472
  _globals['_RFCNBOXPREDICTOR']._serialized_start=2475
  _globals['_RFCNBOXPREDICTOR']._serialized_end=2724
# @@protoc_insertion_point(module_scope)
