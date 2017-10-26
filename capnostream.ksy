meta:
  id: capno
  title: Capnostream Binary Output
  endian: be
doc: |
  This spec defines the data output of the capnostream machines

seq:
  - id: every_message
    type: capno_msg
    #size-eos: true
    #repeat: eos
    repeat: expr
    repeat-expr: 118

types:
  capno_msg:
    seq:
      - id: msg_header
        contents: [0x85]
      - id: msg_length
        type: u1
      - id: msg_code
        type: u1
        enum: cap_codes
      - id: msg_body
        size: msg_length - 1 # msg_code counts as one of the msg_length bytes
        type:
          switch-on: msg_code
          cases:
            'cap_codes::co2_wave_code': co2_wave_msg
            'cap_codes::numerics_code': numerics_msg
            'cap_codes::patient_id_nonunicode_code': patient_id_nonunicode_msg
            'cap_codes::patient_id_unicode_code': patient_id_unicode_msg
            'cap_codes::events_list_nonunicode_code': events_list_nonunicode_msg
            'cap_codes::events_list_unicode_code': events_list_unicode_msg
            'cap_codes::numeric_item_code': numeric_item_msg
            'cap_codes::device_id_and_software_version_code': device_id_and_software_version_msg
            'cap_codes::long_trend_patient_data_download_code': long_trend_patient_data_download__msg
            'cap_codes::new_patient_information_download_nonunicode_code': new_patient_information_download_nonunicode_msg
            'cap_codes::new_patient_information_download_unicode_code': new_patient_information_download_unicode_msg
      - id: chksum
        #size-eos: true
        type: u1 # not actually checking this for validity, but we could in the future
      
      #- id: second_chksum
      #  type: u1
      #  if: _ == 0x80
  co2_wave_msg:
    seq:
      - id: wave_message_number
        type: u1
      - id: instantaneous_co2_value
        type: u2
      - id: fast_status
        type: fast_status_type
  numerics_msg:
    seq:
      - id: timestamp
        type: u4
      - id: etco2_value
        type: u1
      - id: fico2_value
        type: u1
      - id: respiration_rate
        type: u1
      - id: spo2_value
        type: u1
      - id: pulse_rate
        type: u1
      - id: slow_status
        type: slow_status_type
      - id: events_index
        size: 3
      - id: co2_active_alarms
        type: co2_alarm_type
      - id: spo2_active_alarms
        type: spo2_alarm_type
      - id: no_breath_period
        type: u1
      - id: etco2_alarm_high_limit
        type: u1
      - id: etco2_alarm_low_limit
        type: u1
      - id: respiration_rate_alarm_high_limit
        type: u1
      - id: respiration_rate_alarm_low_limit
        type: u1
      - id: fico2_alarm_high_limit
        type: u1
      - id: spo2_alarm_high_limit
        type: u1
      - id: spo2_alarm_low_limit
        type: u1
      - id: pulse_rate_alarm_high_limit
        type: u1
      - id: pulse_rate_alarm_low_limit
        type: u1
      - id: current_capnostream_co2_units
        type: u1
        enum: capnostream_co2_enum
      - id: extended_co2_status
        type: extended_co2_type
  patient_id_nonunicode_msg:
    seq:
      - id: timestamp
        type: u4
      - id: patient_id
        type: str
        size: 24
        encoding: ASCII
  patient_id_unicode_msg:
    seq:
      - id: timestamp
        type: u4
      - id: patient_id
        type: str
        size: 48
        encoding: UTF-8
  events_list_nonunicode_msg:
    seq:
      - id: event_number
        type: u1
      - id: event_description
        type: str
        size: 11
        encoding: ASCII
  events_list_unicode_msg:
    seq:
      - id: event_number
        type: u1
      - id: event_description
        type: str
        size: 22
        encoding: UTF-8
  numeric_item_msg:
    seq:
      - id: response
        type: u1
        enum: ff_invalid_enum
  device_id_and_software_version_msg:
    seq:
      - id: version_num
        type: str
        size: 30
        encoding: ASCII
  long_trend_patient_data_download__msg:
    seq:
      - id: full_trend_download
        type: u1
        repeat: eos
  new_patient_information_download_nonunicode_msg:
    seq:
      - id: timestamp
        type: u4
      - id: patient_id
        type: str
        size: 24
        encoding: ASCII
  new_patient_information_download_unicode_msg:
    seq:
      - id: timestamp
        type: u4
      - id: patient_id
        type: str
        size: 48
        encoding: UTF-8
  fast_status_type:
    seq:
      - id: co2_malfunction
        type: b1
      - id: filterline_not_connected
        type: b1
      - id: purging_in_progress
        type: b1
      - id: sfm_in_progress
        type: b1
      - id: end_of_breath_indication
        type: b1
      - id: occlusion_in_gas_input_line
        type: b1
      - id: initialization
        type: b1
      - id: invalid_co2_value
        type: b1
  slow_status_type:
    seq:
      - id: reserved
        type: b1
        enum: reserved_enum
      - id: pulse_beeps
        type: b1
        enum: zero_audible_enum
      - id: advisory
        type: b1
        enum: zero_silenced_enum
      - id: low_priority_alarm
        type: b1
        enum: zero_silenced_enum
      - id: high_priority_alarm
        type: b1
        enum: zero_silenced_enum
      - id: all_alarms
        type: b1
        enum: zero_audible_enum
      - id: temporary_alarms
        type: b1
        enum: zero_audible_enum
      - id: patient_type
        type: b1
        enum: patient_type_enum
  co2_alarm_type:
    seq:
      - id: reserved
        type: b2
        enum: reserved_enum
      - id: fico2_high
        type: b1
      - id: rr_low
        type: b1
      - id: rr_high
        type: b1
      - id: etco2_low
        type: b1
      - id: etco2_high
        type: b1
      - id: no_breath
        type: b1
  spo2_alarm_type:
    seq:
      - id: reserved
        type: b1
        enum: reserved_enum
      - id: spo2_sensor_disconnected
        type: b1
      - id: spo2_sensor_off_patient
        type: b1
      - id: pulse_rate_low
        type: b1
      - id: pulse_rate_high
        type: b1
      - id: spo2_low
        type: b1
      - id: spo2_high
        type: b1
      - id: pulse_not_found
        type: b1
  extended_co2_type:
    seq:
      - id: reserved
        type: b4
        enum: reserved_enum
      - id: pump_off
        type: b1
      - id: check_flow
        type: b1
      - id: check_calibration
        type: b1

enums:
  cap_codes:
    0: co2_wave_code
    1: numerics_code
    2: patient_id_nonunicode_code
    12: patient_id_unicode_code
    21: events_list_nonunicode_code
    22: events_list_unicode_code
    3: numeric_item_code
    4: device_id_and_software_version_code
    55: long_trend_patient_data_download_code
    57: new_patient_information_download_nonunicode_code
    58: new_patient_information_download_unicode_code
    
  reserved_enum:
    0: reserved
    1: reserved
    2: reserved
    3: reserved
    
    
  zero_silenced_enum:
    0: silenced
    1: audible 
    
  zero_audible_enum:
    0: audible
    1: silenced 
    
  patient_type_enum:
    0: adult
    1: neonate
    
  capnostream_co2_enum:
    1: mmhg
    2: kpa
    3: vol_pct
    
  ff_invalid_enum:
    0xFF: invalid
    