from concurrent.futures import ThreadPoolExecutor

"""
同时处理的最大线程数，本示例中使用线程池
也可以使用进程池ProcessPoolExecutor
"""
executor = ThreadPoolExecutor(5)


def async_executor(_function_, _data_):
    # 执行异步任务
    executor.submit(_function_, _data_)
