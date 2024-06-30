# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/ssd.proto
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
    'object_detection/protos/ssd.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import anchor_generator_pb2 as object__detection_dot_protos_dot_anchor__generator__pb2
from object_detection.protos import box_coder_pb2 as object__detection_dot_protos_dot_box__coder__pb2
from object_detection.protos import box_predictor_pb2 as object__detection_dot_protos_dot_box__predictor__pb2
from object_detection.protos import fpn_pb2 as object__detection_dot_protos_dot_fpn__pb2
from object_detection.protos import hyperparams_pb2 as object__detection_dot_protos_dot_hyperparams__pb2
from object_detection.protos import image_resizer_pb2 as object__detection_dot_protos_dot_image__resizer__pb2
from object_detection.protos import losses_pb2 as object__detection_dot_protos_dot_losses__pb2
from object_detection.protos import matcher_pb2 as object__detection_dot_protos_dot_matcher__pb2
from object_detection.protos import post_processing_pb2 as object__detection_dot_protos_dot_post__processing__pb2
from object_detection.protos import region_similarity_calculator_pb2 as object__detection_dot_protos_dot_region__similarity__calculator__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!object_detection/protos/ssd.proto\x12\x17object_detection.protos\x1a.object_detection/protos/anchor_generator.proto\x1a\'object_detection/protos/box_coder.proto\x1a+object_detection/protos/box_predictor.proto\x1a!object_detection/protos/fpn.proto\x1a)object_detection/protos/hyperparams.proto\x1a+object_detection/protos/image_resizer.proto\x1a$object_detection/protos/losses.proto\x1a%object_detection/protos/matcher.proto\x1a-object_detection/protos/post_processing.proto\x1a:object_detection/protos/region_similarity_calculator.proto\"\xdc\x0b\n\x03Ssd\x12\x13\n\x0bnum_classes\x18\x01 \x01(\x05\x12<\n\rimage_resizer\x18\x02 \x01(\x0b\x32%.object_detection.protos.ImageResizer\x12G\n\x11\x66\x65\x61ture_extractor\x18\x03 \x01(\x0b\x32,.object_detection.protos.SsdFeatureExtractor\x12\x34\n\tbox_coder\x18\x04 \x01(\x0b\x32!.object_detection.protos.BoxCoder\x12\x31\n\x07matcher\x18\x05 \x01(\x0b\x32 .object_detection.protos.Matcher\x12R\n\x15similarity_calculator\x18\x06 \x01(\x0b\x32\x33.object_detection.protos.RegionSimilarityCalculator\x12)\n\x1a\x65ncode_background_as_zeros\x18\x0c \x01(\x08:\x05\x66\x61lse\x12 \n\x15negative_class_weight\x18\r \x01(\x02:\x01\x31\x12<\n\rbox_predictor\x18\x07 \x01(\x0b\x32%.object_detection.protos.BoxPredictor\x12\x42\n\x10\x61nchor_generator\x18\x08 \x01(\x0b\x32(.object_detection.protos.AnchorGenerator\x12@\n\x0fpost_processing\x18\t \x01(\x0b\x32\'.object_detection.protos.PostProcessing\x12+\n\x1dnormalize_loss_by_num_matches\x18\n \x01(\x08:\x04true\x12-\n\x1enormalize_loc_loss_by_codesize\x18\x0e \x01(\x08:\x05\x66\x61lse\x12+\n\x04loss\x18\x0b \x01(\x0b\x32\x1d.object_detection.protos.Loss\x12\x1f\n\x10\x66reeze_batchnorm\x18\x10 \x01(\x08:\x05\x66\x61lse\x12\'\n\x18inplace_batchnorm_update\x18\x0f \x01(\x08:\x05\x66\x61lse\x12\"\n\x14\x61\x64\x64_background_class\x18\x15 \x01(\x08:\x04true\x12(\n\x19\x65xplicit_background_class\x18\x18 \x01(\x08:\x05\x66\x61lse\x12)\n\x1ause_confidences_as_targets\x18\x16 \x01(\x08:\x05\x66\x61lse\x12\"\n\x17implicit_example_weight\x18\x17 \x01(\x02:\x01\x31\x12\x33\n$return_raw_detections_during_predict\x18\x1a \x01(\x08:\x05\x66\x61lse\x12?\n\x10mask_head_config\x18\x19 \x01(\x0b\x32%.object_detection.protos.Ssd.MaskHead\x1a\x84\x03\n\x08MaskHead\x12\x17\n\x0bmask_height\x18\x01 \x01(\x05:\x02\x31\x35\x12\x16\n\nmask_width\x18\x02 \x01(\x05:\x02\x31\x35\x12&\n\x18masks_are_class_agnostic\x18\x03 \x01(\x08:\x04true\x12\'\n\x1amask_prediction_conv_depth\x18\x04 \x01(\x05:\x03\x32\x35\x36\x12*\n\x1fmask_prediction_num_conv_layers\x18\x05 \x01(\x05:\x01\x32\x12+\n\x1c\x63onvolve_then_upsample_masks\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x10mask_loss_weight\x18\x07 \x01(\x02:\x01\x35\x12!\n\x15mask_loss_sample_size\x18\x08 \x01(\x05:\x02\x31\x36\x12>\n\x10\x63onv_hyperparams\x18\t \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\x1d\n\x11initial_crop_size\x18\n \x01(\x05:\x02\x31\x35\"\xeb\x04\n\x13SsdFeatureExtractor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1b\n\x10\x64\x65pth_multiplier\x18\x02 \x01(\x02:\x01\x31\x12\x15\n\tmin_depth\x18\x03 \x01(\x05:\x02\x31\x36\x12>\n\x10\x63onv_hyperparams\x18\x04 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12:\n+override_base_feature_extractor_hyperparams\x18\t \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0fpad_to_multiple\x18\x05 \x01(\x05:\x01\x31\x12#\n\x14use_explicit_padding\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ruse_depthwise\x18\x08 \x01(\x08:\x05\x66\x61lse\x12>\n\x03\x66pn\x18\n \x01(\x0b\x32/.object_detection.protos.FeaturePyramidNetworksH\x00\x12M\n\x05\x62ifpn\x18\x13 \x01(\x0b\x32<.object_detection.protos.BidirectionalFeaturePyramidNetworksH\x00\x12\x34\n%replace_preprocessor_with_placeholder\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\x15\n\nnum_layers\x18\x0c \x01(\x05:\x01\x36\x12\x1e\n\x16spaghettinet_arch_name\x18\x14 \x01(\t\x12\x1c\n\ruse_hardswish\x18\x15 \x01(\x08:\x05\x66\x61lseB\x17\n\x15\x66\x65\x61ture_pyramid_oneofJ\x04\x08\x06\x10\x07')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.ssd_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SSD']._serialized_start=504
  _globals['_SSD']._serialized_end=2004
  _globals['_SSD_MASKHEAD']._serialized_start=1616
  _globals['_SSD_MASKHEAD']._serialized_end=2004
  _globals['_SSDFEATUREEXTRACTOR']._serialized_start=2007
  _globals['_SSDFEATUREEXTRACTOR']._serialized_end=2626
# @@protoc_insertion_point(module_scope)
