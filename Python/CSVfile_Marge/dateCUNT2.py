import pandas as pd
import os
import csv
import re
#내용컷
def csv_line_cut(full_filename_csv,outfile_path_name):
    f = open(full_filename_csv, 'r',newline='',encoding='utf-8')
    reader = csv.reader(f)
    cnt=1
    for row in reader:
        if cnt >= 7:
            f_line = open(outfile_path_name, 'a', newline='',encoding='utf-8')
            wr = csv.writer(f_line)
            wr.writerow(row)
            f_line.close()
        cnt = 1 + cnt
    f.close()
#헤더 생성
def csv_line_header_cut(full_filename_csv,outfile_path_name):
    print("header")
    f = open(full_filename_csv, 'r',newline='',encoding='utf-8')
    reader = csv.reader(f)
    cnt=0
    for row in reader:
        cnt=1+cnt
        if cnt>=1 and cnt<=5:
            f_header = open(outfile_path_name, 'a', newline='',encoding='utf-8')
            wr = csv.writer(f_header)
            wr.writerow(row)
            f_header.close()
    f.close()
    new_header_names = ['Site #', 'Shot #', 'Bin', 'XCoord', 'YCoord', 'CONT_NEG_SDA', 'CONT_NEG_SCL',
                        'CONT_NEG_nEN', 'CONT_NEG_ADDRESS', 'CONT_NEG_TEST', 'CONT_NEG_VDR_5V', 'CONT_NEG_BST2A',
                        'CONT_NEG_BST3A', 'CONT_NEG_BST4A', 'CONT_NEG_BST2B', 'CONT_NEG_BST4B', 'CONT_NEG_nINT',
                        'CONT_NEG_WPC_IN_OK', 'CONT_NEG_SYNC', 'CONT_NEG_GPO', 'CONT_NEG_EXT_5V',
                        'CONT_NEG_VBUS_IN', 'CONT_NEG_CP1A', 'CONT_NEG_CP1A_BOT', 'CONT_NEG_CP1B',
                        'CONT_NEG_CP1B_BOT', 'CONT_NEG_SC_OUT', 'P2P_SHORT_SDA', 'P2P_SHORT_SCL', 'P2P_SHORT_nEN',
                        'P2P_SHORT_ADDRESS', 'P2P_SHORT_TEST', 'P2P_SHORT_VDR_5V', 'P2P_SHORT_BST2A',
                        'P2P_SHORT_BST3A', 'P2P_SHORT_BST4A', 'P2P_SHORT_BST2B', 'P2P_SHORT_BST4B',
                        'P2P_SHORT_nINT', 'P2P_SHORT_WPC_IN_OK', 'P2P_SHORT_SYNC', 'P2P_SHORT_GPO',
                        'P2P_SHORT_EXT_5V', 'P2P_SHORT_VBUS_IN', 'P2P_SHORT_CP1A', 'P2P_SHORT_CP1A_BOT',
                        'P2P_SHORT_CP1B', 'P2P_SHORT_CP1B_BOT', 'P2P_SHORT_SC_OUT', 'IIH_SDA', 'IIH_SCL', 'IIH_nEN',
                        'IIH_ADDRESS', 'IIH_EXT_5V', 'IIL_SDA', 'IIL_SCL', 'IIL_nEN', 'IIL_ADDRESS', 'IIL_EXT_5V',
                        'OTP_PROG_READ_ADD_0', 'OTP_PROG_READ_ADD_1', 'OTP_PROG_READ_ADD_2', 'OTP_PROG_READ_ADD_3',
                        'OTP_PROG_READ_ADD_4', 'OTP_PROG_READ_ADD_5', 'OTP_PROG_READ_ADD_6', 'OTP_PROG_READ_ADD_7',
                        'OTP_PROG_READ_ADD_8', 'OTP_PROG_READ_ADD_9', 'OTP_PROG_READ_ADD_10',
                        'OTP_PROG_READ_ADD_11', 'OTP_PROG_READ_ADD_12', 'OTP_PROG_READ_ADD_13',
                        'OTP_PROG_READ_ADD_14', 'OTP_PROG_READ_ADD_15', 'IQ_VBUS_5p5V', 'IQ_SC_OUT_5p5V', 'nEN_VIH',
                        'nEN_VIL', 'SDA_VIH', 'SDA_VIL', 'SCL_VIH', 'SCL_VIL', 'ADDRESS_VIL', 'ADDRESS_VIH',
                        'SCAN_ASYNC_LV', 'SCAN_CAPTURE_LV', 'SCAN_ASYNC_HV', 'SCAN_CAPTURE_HV', 'BG_TRIM_INIT',
                        'BG_OTP_PROG_READ', 'BG_TRIM_VERIFY_LV', 'BG_TRIM_VERIFY_HV', 'V2I_TRIM_INIT',
                        'V2I_OTP_PROG_READ', 'V2I_TRIM_VERIFY_LV', 'V2I_TRIM_VERIFY_HV', 'FREF_TRIM_INIT',
                        'FREF_OTP_PROG_READ', 'FREF_TRIM_VERIFY_LV', 'FREF_TRIM_VERIFY_HV', 'FSW_TRIM_8_A_LV',
                        'FSW_TRIM_8_B_LV', 'FSW_TRIM_8_A_HV', 'FSW_TRIM_8_B_HV', 'CP_OSC_LV', 'CP_OSC_HV',
                        'VDR_VBUS_IN_LV', 'VDR_VBUS_IN_HV', 'VDR_SC_OUT_LV', 'VDR_SC_OUT_HV', 'VDR_VBUS_IN_DO',
                        'VDR_SC_OUT_DO', 'RDSON_SW1MINIA', 'RDSON_SW1MINIB', 'RDSON_SW1TINYA', 'RDSON_SW1TINYB',
                        'RDSON_SW1A', 'RDSON_SW1B', 'RDSON_SW2MINIA', 'RDSON_SW2MINIB', 'RDSON_SW2A', 'RDSON_SW2B',
                        'RDSON_SW4A', 'RDSON_SW4B', 'RDSON_SW3A', 'RDSON_SW3B', 'AUTO_RECOVERY',
                        'I_VBUS2SC_BYPASS_LV', 'VBUS2SC_BYPASS_LV', 'I_VBUS2SC_BYPASS_HV', 'VBUS2SC_BYPASS_HV',
                        'I_VBUS2SC_SW_LV', 'VBUS2SC_SW_LV', 'I_VBUS2SC_SW_HV', 'VBUS2SC_SW_HV', 'SC2VBUS_BYPASS_LV',
                        'SC2VBUS_BYPASS_HV', 'SC2VBUS_SW_LV', 'SC2VBUS_SW_HV', 'nEN_PULLDOWN', 'GPO_VOH',
                        'GPO_PULLDOWN', 'GPO_VOL', 'nINT_VOH', 'nINT_PULLDOWN', 'nINT_VOL', 'SDA_R', 'SDA_VOL',
                        'WPC_IN_OK_VOL', 'WPC_IN_OK_PULLDOWN', 'WPC_IN_OK_VOH', 'WPC_IN_OK_PULLUP',
                        'VBUS_IN_PULLDOWN', 'I_PCH_STANDBY_LV', 'I_PCH_MAX_LV', 'I_PCH_OFF_LV', 'I_PCH_STANDBY_HV',
                        'I_PCH_MAX_HV', 'I_PCH_OFF_HV', 'I_PDCH_MAX_LV', 'I_PDCH_OFF_LV', 'I_PDCH_MAX_HV',
                        'I_PDCH_OFF_HV', 'THSD_TEMP_TRIM_0_RISING_LV', 'THSD_TEMP_TRIM_0_FALLING_LV',
                        'THSD_TEMP_TRIM_1_RISING_LV', 'THSD_TEMP_TRIM_1_FALLING_LV', 'THSD_TEMP_TRIM_0_RISING_HV',
                        'THSD_TEMP_TRIM_0_FALLING_HV', 'THSD_TEMP_TRIM_1_RISING_HV', 'THSD_TEMP_TRIM_1_FALLING_HV',
                        'VBUS_IN_OK_TH_RISING', 'VBUS_IN_OK_TH_FALLING', 'SC_OUT_OK_TH_RISING',
                        'SC_OUT_OK_TH_FALLING', 'EXT_5V_OK_TH_RISING', 'EXT_5V_OK_TH_FALLING',
                        'VBUS_IN_SWITCH_OK_TH_RISING', 'VBUS_IN_SWITCH_OK_TH_FALLING', 'VBUS_IN_MAX_OV_0_TH_RISING',
                        'VBUS_IN_MAX_OV_0_TH_FALLING', 'VBUS_IN_MAX_OV_1_TH_RISING', 'VBUS_IN_MAX_OV_1_TH_FALLING',
                        'SC_OUT_MAX_OV_0_TH_RISING', 'SC_OUT_MAX_OV_0_TH_FALLING', 'SC_OUT_MAX_OV_1_TH_RISING',
                        'SC_OUT_MAX_OV_1_TH_FALLING', 'VBUS_IN_UV_TRACK_SW_UV00_RISING',
                        'VBUS_IN_UV_TRACK_SW_UV00_FALLING', 'VBUS_IN_UV_TRACK_SW_UV01_RISING',
                        'VBUS_IN_UV_TRACK_SW_UV01_FALLING', 'VBUS_IN_UV_TRACK_SW_UV10_RISING',
                        'VBUS_IN_UV_TRACK_SW_UV10_FALLING', 'VBUS_IN_UV_TRACK_SW_UV11_RISING',
                        'VBUS_IN_UV_TRACK_SW_UV11_FALLING', 'VBUS_IN_UV_TRACK_BP_UV00_RISING',
                        'VBUS_IN_UV_TRACK_BP_UV00_FALLING', 'VBUS_IN_UV_TRACK_BP_UV01_RISING',
                        'VBUS_IN_UV_TRACK_BP_UV01_FALLING', 'VBUS_IN_UV_TRACK_BP_UV10_RISING',
                        'VBUS_IN_UV_TRACK_BP_UV10_FALLING', 'VBUS_IN_UV_TRACK_BP_UV11_RISING',
                        'VBUS_IN_UV_TRACK_BP_UV11_FALLING', 'VBUS_IN_OV_TRACK_SW_OV00_RISING',
                        'VBUS_IN_OV_TRACK_SW_OV00_FALLING', 'VBUS_IN_OV_TRACK_SW_OV01_RISING',
                        'VBUS_IN_OV_TRACK_SW_OV01_FALLING', 'VBUS_IN_OV_TRACK_SW_OV10_RISING',
                        'VBUS_IN_OV_TRACK_SW_OV10_FALLING', 'VBUS_IN_OV_TRACK_SW_OV11_RISING',
                        'VBUS_IN_OV_TRACK_SW_OV11_FALLING', 'VBUS_IN_OV_TRACK_BP_OV00_RISING',
                        'VBUS_IN_OV_TRACK_BP_OV00_FALLING', 'VBUS_IN_OV_TRACK_BP_OV01_RISING',
                        'VBUS_IN_OV_TRACK_BP_OV01_FALLING', 'VBUS_IN_OV_TRACK_BP_OV10_RISING',
                        'VBUS_IN_OV_TRACK_BP_OV10_FALLING', 'VBUS_IN_OV_TRACK_BP_OV11_RISING',
                        'VBUS_IN_OV_TRACK_BP_OV11_FALLING', 'POST_CONT_NEG_SDA', 'POST_CONT_NEG_SCL',
                        'POST_CONT_NEG_nEN', 'POST_CONT_NEG_ADDRESS', 'POST_CONT_NEG_TEST', 'POST_CONT_NEG_VDR_5V',
                        'POST_CONT_NEG_BST2A', 'POST_CONT_NEG_BST3A', 'POST_CONT_NEG_BST4A', 'POST_CONT_NEG_BST2B',
                        'POST_CONT_NEG_BST4B', 'POST_CONT_NEG_nINT', 'POST_CONT_NEG_WPC_IN_OK',
                        'POST_CONT_NEG_SYNC', 'POST_CONT_NEG_GPO', 'POST_CONT_NEG_EXT_5V', 'POST_CONT_NEG_VBUS_IN',
                        'POST_CONT_NEG_CP1A', 'POST_CONT_NEG_CP1A_BOT', 'POST_CONT_NEG_CP1B',
                        'POST_CONT_NEG_CP1B_BOT', 'POST_CONT_NEG_SC_OUT', 'POST_P2P_SHORT_SDA',
                        'POST_P2P_SHORT_SCL', 'POST_P2P_SHORT_nEN', 'POST_P2P_SHORT_ADDRESS', 'POST_P2P_SHORT_TEST',
                        'POST_P2P_SHORT_VDR_5V', 'POST_P2P_SHORT_BST2A', 'POST_P2P_SHORT_BST3A',
                        'POST_P2P_SHORT_BST4A', 'POST_P2P_SHORT_BST2B', 'POST_P2P_SHORT_BST4B',
                        'POST_P2P_SHORT_nINT', 'POST_P2P_SHORT_WPC_IN_OK', 'POST_P2P_SHORT_SYNC',
                        'POST_P2P_SHORT_GPO', 'POST_P2P_SHORT_EXT_5V', 'POST_P2P_SHORT_VBUS_IN',
                        'POST_P2P_SHORT_CP1A', 'POST_P2P_SHORT_CP1A_BOT', 'POST_P2P_SHORT_CP1B',
                        'POST_P2P_SHORT_CP1B_BOT', 'POST_P2P_SHORT_SC_OUT', 'POST_IIH_SDA', 'POST_IIH_SCL',
                        'POST_IIH_nEN', 'POST_IIH_ADDRESS', 'POST_IIH_EXT_5V', 'POST_IIL_SDA', 'POST_IIL_SCL',
                        'POST_IIL_nEN', 'POST_IIL_ADDRESS', 'POST_IIL_EXT_5V', 'POST_IQ_VBUS_5p5V',
                        'DELTA_IQ_VBUS_5p5V', 'POST_IQ_SC_OUT_5p5V', 'DELTA_IQ_SC_OUT_5p5V']
    f_sub_header = open(outfile_path_name, 'a', newline='', encoding='utf-8')
    wr = csv.writer(f_sub_header)
    wr.writerow(new_header_names)
    f_sub_header.close()
    print(new_header_names)



#대형 디렉토리 안 CSV 파일 이름 추출
def search_csv(full_filename,outfile_path_name):
    filenames = os.listdir(full_filename)
    cnt=0
    for filename in filenames:
        full_filename_csv = os.path.join(full_filename, filename)
        ext = os.path.splitext(full_filename_csv)[-1]
        if ext == '.csv':
            print(filename)
            print(full_filename_csv)
            print(cnt)
            #print(re.split('_W',filename))
            if cnt==0:
                csv_line_header_cut(full_filename_csv,outfile_path_name)
                print(cnt)
                print("dddd")

            csv_line_cut(full_filename_csv,outfile_path_name)
            cnt = cnt + 1


#대형 디렉토리
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        #print(full_filename)
        print(full_filename)
        filename = full_filename[full_filename.rfind('\\') + 1:]
        outfile_path_name=os.getcwd()+"\\OUTPUT\\"+filename+".csv"
        print(outfile_path_name)
        search_csv(full_filename,outfile_path_name)




search(os.getcwd()+"\\INPUT")
