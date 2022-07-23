import os

from threading import Thread


class YTMultithreading:
    def run_multi_threading(self, target, data, inputs):
        threads = []
        threads_num = os.cpu_count()
        if data:
            data_equla_parts = self.iterable_data_equal_parts(data, threads_num)

        for core in range(threads_num):
            # print('thread:', core, 'create')
            if not data:
                threads.append(Thread(target=target))
            else:
                threads.append(Thread(target=target, args=data_equla_parts[core], kwargs=inputs))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def iterable_data_equal_parts(self, iterable_data, threads_num):
        equal_parts_num = int(len(iterable_data) / threads_num)
        if len(iterable_data) % threads_num != 0:
            equal_parts_num += 1
        return tuple([iterable_data[i:i + equal_parts_num] for i in range(0, len(iterable_data), equal_parts_num)])
