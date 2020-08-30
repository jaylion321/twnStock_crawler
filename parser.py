import os
import requests
import pandas as pd 
import time
import logging

# to_numeric for multi col: https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
#  https://chrisalbon.com/python/data_wrangling/pandas_selecting_rows_on_conditions/

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.ERROR, filename='ERROR.log', filemode='a+', format=FORMAT)
# 公司績效
def Get_Stock_Performance_From_Web(code=None,delay=15,log='Y'):
    logging.basicConfig(format=FORMAT)
    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID='+str(code)+'&YEAR_PERIOD=9999&RPT_CAT=M%5FYEAR&STEP=DATA&SHEET=%E7%8D%B2%E5%88%A9%E6%8C%87%E6%A8%99'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            ,'Origin' : "https://goodinfo.tw"
            ,'Cookie': 'CLIENT%5FID=20200621212410210%5F1%2E34%2E220%2E125; _ga=GA1.2.1444732323.1592745938; SCREEN_SIZE=WIDTH=1600&HEIGHT=900; _gid=GA1.2.285344529.1594435008'
            ,'Referer' : 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=1110'}
    try:
        r = requests.get(url,headers = headers)
        time.sleep(delay)
        r.encoding = 'utf-8'
        data_frame = pd.read_html(r.text)
        return data_frame[1]
    except Exception  as e:
        print(e)
        if (log == 'Y'):
            logging.error('[Get performance]Stock code: %d',code, exc_info=True)
            logging.error('======================================', exc_info=True)

def Get_Stock_Performance_yeild_From_Web(code=None,delay=15,log='Y'):
    logging.basicConfig(format=FORMAT)
    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID='+str(code)+'&YEAR_PERIOD=9999&RPT_CAT=M%5FYEAR&STEP=DATA&SHEET=%E8%82%A1%E5%88%A9%E7%B5%B1%E8%A8%88'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            ,'Origin' : "https://goodinfo.tw"
            ,'Cookie': 'CLIENT%5FID=20200621212410210%5F1%2E34%2E220%2E125; _ga=GA1.2.1444732323.1592745938; SCREEN_SIZE=WIDTH=1280&HEIGHT=720; GOOD%5FINFO%5FSTOCK%5FBROWSE%5FLIST=4%7C8024%7C4961%7C8271%7C2330; _gid=GA1.2.2133515932.1595079244'
            ,'Referer' : 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330'}
    try:
        r = requests.get(url,headers = headers)
        time.sleep(delay)
        r.encoding = 'utf-8'
        data_frame = pd.read_html(r.text)
        return data_frame[1]
    except Exception  as e:
        print(e)
        if (log == 'Y'):
            logging.error('[Get yield]Stock code: %d',code, exc_info=True)
            logging.error('++++++++++++++++++++++++++++++++++++++', exc_info=True)

def Get_Stock_Performance_PER_PBR_From_Web(code=None,delay=15,log='Y'):
    logging.basicConfig(format=FORMAT)
    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID='+str(code)+'&YEAR_PERIOD=9999&RPT_CAT=M%5FYEAR&STEP=DATA&SHEET=PER%2FPBR'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            ,'Origin' : "https://goodinfo.tw"
            ,'Cookie': 'CLIENT%5FID=20200621212410210%5F1%2E34%2E220%2E125; _ga=GA1.2.1444732323.1592745938; SCREEN_SIZE=WIDTH=1280&HEIGHT=720; GOOD%5FINFO%5FSTOCK%5FBROWSE%5FLIST=4%7C8024%7C4961%7C8271%7C2330; _gid=GA1.2.2133515932.1595079244'
            ,'Referer' : 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330'}
    try:
        r = requests.get(url,headers = headers)
        time.sleep(delay)
        r.encoding = 'utf-8'
        data_frame = pd.read_html(r.text)
        return data_frame[1]
    except Exception  as e:
        print("error:",code)
        if (log == 'Y'):
            logging.error('[Get PER_PBR]Stock code: %d',code, exc_info=True)
            logging.error('=====================================', exc_info=True)

def Get_Stock_Performance_From_CSV(path=None, dir_list=None,code=None):
    if ("performace_"+str(code)+'.csv' in dir_list):
        mutiindex_list = []
        cnt = 0
        df_performance = pd.read_csv(path)

        # search first row of data 
        for value in df_performance['年度']:
            if value == '年度':
                cnt = cnt + 1 

        df_performance = pd.read_csv(path,header=(list(range(cnt+1))))
        # drop duplicated level
        df_performance.columns = df_performance.columns.droplevel(list(range(2,cnt+1)))
        # print(df_performance.columns)
        # print(df_performance[])
        # df_performance.rename(columns=dict(zip(df_performance.columns[1:],  mutiindex_list[1:]  )),inplace=True)
        
        # df_performance.rename(columns=dict(zip(df_performance.columns[1:],  mutiindex_list  )),inplace=True)
        # for colume_lv2 in df_performance.loc[0,:][1:]:
        #     # print (colume_lv2)
        #     mutiindex_list.append(colume_lv2)  
        # for colume_lv1,colume_lv2,colume_lv3,colume_lv4 in zip(df_performance.columns[1:], (df_performance.loc[0,:])[1:], (df_performance.loc[1,:])[1:], (df_performance.loc[2,:])[1:]):
        #     mutiindex_list += [tuple( [colume_lv1,colume_lv2,colume_lv3,colume_lv4])]       
        # df_performance.rename(columns=dict(zip(df_performance.columns[1:],  mutiindex_list  )),inplace=True)
        # df_performance = df_performance.drop(range(cnt))
        return df_performance
    else:
        return None

def Get_Stock_Performance_yeild_From_CSV(path=None, dir_list=None,code=None):
    if ("yeild_"+str(code)+'.csv' in dir_list):  
        mutiindex_list = []
        cnt = 0
        df_yeild = pd.read_csv(path)
        # search first row of data 
        for value in df_yeild['年度']:
            if value == '年度':
                cnt = cnt + 1 
        df_yeild = pd.read_csv(path,header=(list(range(cnt+1))))
        # drop duplicated level
        df_yeild.columns = df_yeild.columns.droplevel(list(range(2,cnt+1)))

        # for colume_lv2 in df_yeild.loc[0,:][1:]:
        #     mutiindex_list.append(colume_lv2)
        # df_yeild.rename(columns=dict(zip(df_yeild.columns[1:],  mutiindex_list  )),inplace=True)
        # df_yeild = df_yeild.drop(range(cnt))        
        return df_yeild
    else:
        return None

def Get_Stock_Performance_PER_PBR_From_CSV(path=None, dir_list=None,code=None):
    if ("per_pbr_"+str(code)+'.csv' in dir_list):
        mutiindex_list = []
        cnt = 0
        df_per = pd.read_csv(path)

        # search first row of data 
        for value in df_per['年度']:
            if value == '年度':
                cnt = cnt + 1 
        df_per = pd.read_csv(path,header=(list(range(cnt+1))))
        # drop duplicated level
        df_per.columns = df_per.columns.droplevel(list(range(2,cnt+1)))
        return df_per
    else:
        return None


def Get_value_by_IDX_as_float(concate_table=None,col_idx=None):
    if ( type(concate_table).__name__ == 'NoneType'):
        return None
    #using apply to transfer type of multiple columns 
    #pd.to_numeric: cast to float, error to be NAN
    return concate_table.loc[:,col_idx].apply(pd.to_numeric,downcast='float', errors='coerce')
     

def Concat_Table_Index(concate_table,year='2016', idx_list =  [tuple(['年度股價(元)','收盤']),tuple(['年度股價(元)','最低']),tuple(['年度股價(元)','最高']),tuple(['年度股價(元)','平均']),tuple(['股利政策(元)','現金']),tuple(['EPS(元)','稅後EPS']), tuple(['ROA(%)','ROA(%)']) ,tuple(['ROE(%)','ROE(%)']),tuple(['BPS(元)','BPS(元)']),tuple(['本益比(PER)統計','平均PER']),tuple(['本淨比(PBR)統計','最高PBR'])]):
    # remove duplicated columns ,or we can not refer value by colunms
    concate_table = concate_table.loc[:,~concate_table.columns.duplicated()]
    # print (concate_table.columns)
    # idx_list = [tuple(['EPS(元)','稅後EPS']), tuple(['ROA(%)','ROA(%)']) ,tuple(['ROE(%)','ROE(%)']),tuple(['BPS(元)','BPS(元)']),tuple(['本益比(PER)統計','平均PER']),tuple(['本淨比(PBR)統計','最高PBR'])]
    table = [concate_table,concate_table,concate_table,concate_table,concate_table,concate_table,concate_table,concate_table,concate_table,concate_table]
   

    con =  pd.concat([ concate_table.loc[:,tuple(['年度','年度'])]]+ list(map(Get_value_by_IDX_as_float,table,idx_list)),axis=1)
    idx = con.loc[con['年度']['年度'] ==year,:].index.values
    if len(idx) != 0:
        return con.loc[0:idx[0],:]
    else:
        print("Please check input of years")
        return None

    # print(concate_table['EPS(元)'])
    # print(concate_table.loc[: , tuple(['EPS(元)','稅後EPS'])])
    # print (concate_table.loc[: ,( concate_table['EPS(元)']['稅後EPS']=='-') ]   )
    # for val in concate_table['EPS(元)']['稅後EPS']:
    #     print (float(val))
    # print(concate_table['EPS(元)']['稅後EPS'])

    # Get_value_by_IDX(concate_table, tuple(['年度','年度']) )
    

    # print( concate_table['EPS(元)']['稅後EPS'])

def Concat_Table_With_IDX(path = None, code = None, idx_list = None):
    if ( path == None or code == None):
        return -1
    dataframe_dir = {}
    dir_list = os.listdir(path)
    for dir_name in dir_list:
        if (str(code)  in dir_name):
            path = path +  '/' + dir_name
    dir_list = os.listdir(path)


    df_performance = Get_Stock_Performance_From_CSV(path+ "/performace_"+str(code)+'.csv',dir_list,code)
    dataframe_dir['performance'] = df_performance

    df_per = Get_Stock_Performance_PER_PBR_From_CSV(path+ "/per_pbr_"+str(code)+'.csv',dir_list,code)
    dataframe_dir['per'] = df_per


  
    df_yeild = Get_Stock_Performance_yeild_From_CSV(path+"/yeild_"+str(code)+'.csv',dir_list,code)
    dataframe_dir['yield'] = df_yeild


    for key,value in dataframe_dir.items():
        if ( type(dataframe_dir[key]).__name__ == 'NoneType') :
            print(key+ " : There is no table")
            return dataframe_dir


    
    #concate without checking duplicated columns
    concate_table = pd.concat([ dataframe_dir['performance'],dataframe_dir['yield'].iloc[:,11:],dataframe_dir['per'].iloc[:,4:]],axis=1)
   
    concate_table = Concat_Table_Index(concate_table)

    # print(concate_table)
    if ( type(concate_table).__name__ == 'DataFrame') :
        num_of_positive_eps = (concate_table['EPS(元)']['稅後EPS'][1:,] > 1).sum()
        if (num_of_positive_eps == 4):
            print(concate_table)
    else:
        print(code," : Error")
    # print (dataframe_dir['performance'].columns)
    # print ( list(zip( *['a','b'])) )
    # for label, content in dataframe_dir['performance'].items():
    #     print ('label:', label[1])
        # print (content[:])
    # print(concate_table)


if __name__ == "__main__":
    print ("end")