import os

from multiprocessing import Process


class YTMultiProcessing:
    def run_multi_processing(self, target, data, inputs):
        processes = []
        process_num = os.cpu_count()
        if data:
            data_equla_parts = self.iterable_data_equal_parts(data, process_num)

        for core in range(process_num):
            # print('process:', core, 'create')
            if not data:
                processes.append(Process(target=target))
            else:
                processes.append(Process(target=target, args=data_equla_parts[core], kwargs=inputs))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    def iterable_data_equal_parts(self, iterable_data, process_num):
        equal_parts_num = int(len(iterable_data) / process_num)
        if len(iterable_data) % process_num != 0:
            equal_parts_num += 1
        return tuple([iterable_data[i:i + equal_parts_num] for i in range(0, len(iterable_data), equal_parts_num)])
