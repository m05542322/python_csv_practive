# encoding: utf-8
#!/usr/bin/python

class final_data:
    def __init__(self, sso_id, account_name, country_code, cellphone, email, display_name,
                 total_usage, week_upload_frquency, month_upload_frequency, registration_date, lastest_login_date, platform, language):
        self.sso_id = sso_id
	self.account_name = account_name
        self.country_code = country_code
        self.cellphone = cellphone
        self.email = email
        self.display_name = display_name
        self.total_usage = total_usage
        self.week_upload_frquency = week_upload_frquency
        self.month_upload_frequency = month_upload_frequency
        self.registration_date = registration_date
        self.lastest_login_date = lastest_login_date
        self.platform = platform
        self.language = language
    def get_item(self):
        return self.sso_id + ', ' + \
		self.account_name + ', ' + \
                self.country_code + ', ' + \
                self.cellphone + ', ' + \
                self.email + ', ' + \
                self.display_name + ', ' + \
                self.total_usage + ', ' + \
                self.week_upload_frquency + ', ' + \
                self.month_upload_frequency + ', ' + \
                self.registration_date + ', ' + \
                self.lastest_login_date + ', ' + \
                self.platform + ', ' + \
                self.language

class sso_data:
    def __init__(self, account_name, country_code, cellphone, email, display_name, sso_id, registration_date, lastest_login_date, platform, language):
        self.account_name = account_name
        self.country_code = country_code
        self.cellphone = cellphone
        self.email = email
        self.display_name = display_name
        self.sso_id = sso_id
        self.registration_date = registration_date
        self.lastest_login_date = lastest_login_date
        self.platform = platform
        self.language = language
    
class metadata_data:
    def __init__(self, owner_id, total_usage, week_upload_frquency, month_upload_frequency):
        self.owner_id = owner_id
        self.total_usage = total_usage
        self.week_upload_frquency = week_upload_frquency
        self.month_upload_frequency = month_upload_frequency

baseFilePath = '/home/tim/box_usage_report/'

# set file name
newegg_user = [baseFilePath + 'newegg_user.csv',baseFilePath + 'metadata.csv', baseFilePath + 'output_newegg_user.csv']
not_newegg_user = [baseFilePath + 'none_newegg_user.csv', baseFilePath + 'metadata.csv', baseFilePath + 'output_none_newegg_user.csv']
total_list = [newegg_user, not_newegg_user]


for item in total_list:
    '''
    input source_newegg_user.csv/source_not_newegg_user.csv file format
    account_name, country_code, cellphone, email, display_name, sso_id, registration_date, lastest_login_date, platform, language
    953721867,886,953721867,p0953721867@yahoo.com.tw,MyBox,2eb6153a4337e5a97bdc56efad81cf4e,2015/8/16 13:52,2015/8/16 13:52, android, zh_tw
    '''
    with open (item[0], 'rb') as sso_in:
        c_sso_in = sso_in.readlines()
        sso = [ 0 for i in xrange(len(c_sso_in))]
        i=0
        for line in c_sso_in:
            line = line.split('\n')[0]
            data = line.split(',')
            sso[i] = sso_data(data[0].strip(), # account_name
                              data[1].strip(), # country_code
                              data[2].strip(), # cellphone
                              data[3].strip(), # email
                              data[4].strip(), # display_name
                              data[5].strip(), # sso_id
                              data[6].strip(), # registration_date
                              data[7].strip(), # lastest_login_date
                              data[8].strip(), # platform
                              data[9].strip()  # language
                            )
            i+=1
        sso_in.close()
    '''
    input source_metadata.csv file format
    owner_id,total_usage(MB),week_upload_frequency,month_upload_frequency
    2eb6153a4337e5a97bdc56efad81cf4e,12.195,33,33
    '''
    with open (item[1], 'rb') as meta_in:
        c_meta_in = meta_in.readlines()
        meta = [ 0 for i in xrange(len(c_meta_in))]
        i=0
        for line in c_meta_in:
            line = line.split('\n')[0]
            data = line.split(',')
            meta[i] = metadata_data(data[0].strip(), # owner_id
                                    data[1].strip(), # total_usage(MB)
                                    data[2].strip(), # week_upload_frequency
                                    data[3].strip()) # month_upload_frequency
            i+=1
        meta_in.close()

    '''
    output .csv file format
    account_name,country_code,cellphone,email,display_name,total_usage(MB),week_upload_frequency,month_upload_frequency,registration_date,lastest_login_date
    953721867,886,953721867,p0953721867@yahoo.com.tw,MyBox,12.195,33,33,2015/8/16 13:52,2015/8/16 13:52
    '''
    with open (item[2], 'wb') as output:
            output.write('sso_id,account_name,country_code,cellphone,email,display_name, \
                         total_usage(MB),week_upload_frequency,month_upload_frequency,registration_date,lastest_login_date,platform,language\n')
            for i in xrange(len(sso)):
                for j in xrange(len(meta)):
                    if sso[i].sso_id == meta[j].owner_id:
                        line = final_data(sso[i].sso_id,
					  sso[i].account_name,
                                          sso[i].country_code,
                                          sso[i].cellphone,
                                          sso[i].email,
                                          sso[i].display_name,
                                          meta[j].total_usage,
                                          meta[j].week_upload_frquency,
                                          meta[j].month_upload_frequency,
                                          sso[i].registration_date,
                                          sso[i].lastest_login_date,
                                          sso[i].platform,
                                          sso[i].language
                                        )
			print "========================================================================="
                        print sso[i].sso_id,sso[i].account_name,sso[i].country_code,sso[i].cellphone,sso[i].email,sso[i].display_name,meta[j].total_usage,meta[j].week_upload_frquency,meta[j].month_upload_frequency,sso[i].registration_date,sso[i].lastest_login_date, sso[i].platform, sso[i].language
                        output.write(line.get_item())
                        output.write('\n')
            output.close()

