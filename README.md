# twnStock_crawler
目前是以Synchronous request 的 libray requests 來coding

### Todo List
#### 同時開多個request
##### 1.Get Free Proxy server list
    [How to get valid proxy](https://codelike.pro/create-a-crawler-with-rotating-ip-proxy-in-python/) 
##### 2. Send Multiple Request simultaneously  
```
主要 ： Asynchronous requests(aiohttp)
    aiohttp : Proxy 目前不支援https, only support http
備案 ： Synchronous request + process(requests + multiprocessing) 
    Multiprocess example
        pool = Pool(4)
        start = time.time()
        #callback get result in order
        results = pool.starmap_async(main_map, [(1,1),(2,2),(3,0),(4,3),(5,3),(6,5),(7,1),(8,0)],callback=show)
        pool.close()
        pool.join()
        
   starmap_async vs map_async
   starmap_async : Support multi args
   map_async  :    can only one args
   
```

    
   
