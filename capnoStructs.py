# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import array
import struct
import zlib
from enum import Enum
from pkg_resources import parse_version

from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Capno(KaitaiStruct):

    class PatientTypeEnum(Enum):
        adult = 0
        neonate = 1

    class ReservedEnum(Enum):
        reserved = 0

    class ZeroSilencedEnum(Enum):
        silenced = 0
        audible = 1

    class CapCodes(Enum):
        co2_wave_code = 0
        numerics_code = 1
        patient_id_nonunicode_code = 2
        numeric_item_code = 3
        device_id_and_software_version_code = 4
        patient_id_unicode_code = 12
        events_list_nonunicode_code = 21
        events_list_unicode_code = 22
        long_trend_patient_data_download_code = 55
        new_patient_information_download_nonunicode_code = 57
        new_patient_information_download_unicode_code = 58

    class FfInvalidEnum(Enum):
        invalid = 255

    class ZeroAudibleEnum(Enum):
        audible = 0
        silenced = 1

    class CapnostreamCo2Enum(Enum):
        mmhg = 1
        kpa = 2
        vol_pct = 3
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.every_message = [None] * (10)
        for i in range(10):
            self.every_message[i] = self._root.CapnoMsg(self._io, self, self._root)


    class SlowStatusType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.reserved = self._root.ReservedEnum(self._io.read_bits_int(1))
            self.pulse_beeps = self._root.ZeroAudibleEnum(self._io.read_bits_int(1))
            self.advisory = self._root.ZeroSilencedEnum(self._io.read_bits_int(1))
            self.low_priority_alarm = self._root.ZeroSilencedEnum(self._io.read_bits_int(1))
            self.high_priority_alarm = self._root.ZeroSilencedEnum(self._io.read_bits_int(1))
            self.all_alarms = self._root.ZeroAudibleEnum(self._io.read_bits_int(1))
            self.temporary_alarms = self._root.ZeroAudibleEnum(self._io.read_bits_int(1))
            self.patient_type = self._root.PatientTypeEnum(self._io.read_bits_int(1))


    class Co2WaveMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.wave_message_number = self._io.read_u1()
            self.instantaneous_co2_value = self._io.read_u2be()
            self.fast_status = self._root.FastStatusType(self._io, self, self._root)


    class NumericItemMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.response = self._root.FfInvalidEnum(self._io.read_u1())


    class Spo2AlarmType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.reserved = self._root.ReservedEnum(self._io.read_bits_int(1))
            self.spo2_sensor_disconnected = self._io.read_bits_int(1) != 0
            self.spo2_sensor_off_patient = self._io.read_bits_int(1) != 0
            self.pulse_rate_low = self._io.read_bits_int(1) != 0
            self.pulse_rate_high = self._io.read_bits_int(1) != 0
            self.spo2_low = self._io.read_bits_int(1) != 0
            self.spo2_high = self._io.read_bits_int(1) != 0
            self.pulse_not_found = self._io.read_bits_int(1) != 0


    class EventsListUnicodeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.event_number = self._io.read_u1()
            self.event_description = (self._io.read_bytes(22)).decode(u"UTF-8")


    class FastStatusType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.co2_malfunction = self._io.read_bits_int(1) != 0
            self.filterline_not_connected = self._io.read_bits_int(1) != 0
            self.purging_in_progress = self._io.read_bits_int(1) != 0
            self.sfm_in_progress = self._io.read_bits_int(1) != 0
            self.end_of_breath_indication = self._io.read_bits_int(1) != 0
            self.occlusion_in_gas_input_line = self._io.read_bits_int(1) != 0
            self.initialization = self._io.read_bits_int(1) != 0
            self.invalid_co2_value = self._io.read_bits_int(1) != 0


    class DeviceIdAndSoftwareVersionMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.version_num = (self._io.read_bytes(30)).decode(u"ASCII")


    class ExtendedCo2Type(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.reserved = self._root.ReservedEnum(self._io.read_bits_int(4))
            self.pump_off = self._io.read_bits_int(1) != 0
            self.check_flow = self._io.read_bits_int(1) != 0
            self.check_calibration = self._io.read_bits_int(1) != 0


    class NewPatientInformationDownloadUnicodeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.timestamp = self._io.read_u4be()
            self.patient_id = (self._io.read_bytes(48)).decode(u"UTF-8")


    class PatientIdNonunicodeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.timestamp = self._io.read_u4be()
            self.patient_id = (self._io.read_bytes(24)).decode(u"ASCII")


    class Co2AlarmType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.reserved = self._root.ReservedEnum(self._io.read_bits_int(2))
            self.fico2_high = self._io.read_bits_int(1) != 0
            self.rr_low = self._io.read_bits_int(1) != 0
            self.rr_high = self._io.read_bits_int(1) != 0
            self.etco2_low = self._io.read_bits_int(1) != 0
            self.etco2_high = self._io.read_bits_int(1) != 0
            self.no_breath = self._io.read_bits_int(1) != 0


    class NewPatientInformationDownloadNonunicodeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.timestamp = self._io.read_u4be()
            self.patient_id = (self._io.read_bytes(24)).decode(u"ASCII")


    class CapnoMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.msg_header = self._io.ensure_fixed_contents(struct.pack('1b', -123))
            self.msg_length = self._io.read_u1()
            self.msg_code = self._root.CapCodes(self._io.read_u1())
            _on = self.msg_code
            if _on == self._root.CapCodes.new_patient_information_download_unicode_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.NewPatientInformationDownloadUnicodeMsg(io, self, self._root)
            elif _on == self._root.CapCodes.numeric_item_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.NumericItemMsg(io, self, self._root)
            elif _on == self._root.CapCodes.events_list_nonunicode_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.EventsListNonunicodeMsg(io, self, self._root)
            elif _on == self._root.CapCodes.new_patient_information_download_nonunicode_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.NewPatientInformationDownloadNonunicodeMsg(io, self, self._root)
            elif _on == self._root.CapCodes.patient_id_nonunicode_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.PatientIdNonunicodeMsg(io, self, self._root)
            elif _on == self._root.CapCodes.device_id_and_software_version_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.DeviceIdAndSoftwareVersionMsg(io, self, self._root)
            elif _on == self._root.CapCodes.events_list_unicode_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.EventsListUnicodeMsg(io, self, self._root)
            elif _on == self._root.CapCodes.long_trend_patient_data_download_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.LongTrendPatientDataDownloadMsg(io, self, self._root)
            elif _on == self._root.CapCodes.numerics_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.NumericsMsg(io, self, self._root)
            elif _on == self._root.CapCodes.patient_id_unicode_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.PatientIdUnicodeMsg(io, self, self._root)
            elif _on == self._root.CapCodes.co2_wave_code:
                self._raw_msg_body = self._io.read_bytes((self.msg_length - 1))
                io = KaitaiStream(BytesIO(self._raw_msg_body))
                self.msg_body = self._root.Co2WaveMsg(io, self, self._root)
            else:
                self.msg_body = self._io.read_bytes((self.msg_length - 1))
            self.chksum = self._io.read_u1()


    class EventsListNonunicodeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.event_number = self._io.read_u1()
            self.event_description = (self._io.read_bytes(11)).decode(u"ASCII")


    class LongTrendPatientDataDownloadMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.full_trend_download = []
            while not self._io.is_eof():
                self.full_trend_download.append(self._io.read_u1())



    class PatientIdUnicodeMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.timestamp = self._io.read_u4be()
            self.patient_id = (self._io.read_bytes(48)).decode(u"UTF-8")


    class NumericsMsg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.timestamp = self._io.read_u4be()
            self.etco2_value = self._io.read_u1()
            self.fico2_value = self._io.read_u1()
            self.respiration_rate = self._io.read_u1()
            self.spo2_value = self._io.read_u1()
            self.pulse_rate = self._io.read_u1()
            self.slow_status = self._root.SlowStatusType(self._io, self, self._root)
            self.events_index = self._io.read_bytes(3)
            self.co2_active_alarms = self._root.Co2AlarmType(self._io, self, self._root)
            self.spo2_active_alarms = self._root.Spo2AlarmType(self._io, self, self._root)
            self.no_breath_period = self._io.read_u1()
            self.etco2_alarm_high_limit = self._io.read_u1()
            self.etco2_alarm_low_limit = self._io.read_u1()
            self.respiration_rate_alarm_high_limit = self._io.read_u1()
            self.respiration_rate_alarm_low_limit = self._io.read_u1()
            self.fico2_alarm_high_limit = self._io.read_u1()
            self.spo2_alarm_high_limit = self._io.read_u1()
            self.spo2_alarm_low_limit = self._io.read_u1()
            self.pulse_rate_alarm_high_limit = self._io.read_u1()
            self.pulse_rate_alarm_low_limit = self._io.read_u1()
            self.current_capnostream_co2_units = self._root.CapnostreamCo2Enum(self._io.read_u1())
            self.extended_co2_status = self._root.ExtendedCo2Type(self._io, self, self._root)