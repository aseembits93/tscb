import pickle
import os
def _log__test__values(values, duration, test_name):
    iteration = os.environ["CODEFLASH_TEST_ITERATION"]
    with open(os.path.join('/var/folders/gt/6989l91x4ls_47vdhp33t7sm0000gn/T/codeflash_ot0x0mej/', f'test_return_values_{iteration}.bin'), 'ab') as f:
        return_bytes = pickle.dumps(values)
        _test_name = f"{test_name}".encode("ascii")
        f.write(len(_test_name).to_bytes(4, byteorder='big'))
        f.write(_test_name)
        f.write(duration.to_bytes(8, byteorder='big'))
        f.write(len(return_bytes).to_bytes(4, byteorder='big'))
        f.write(return_bytes)
import time
import gc
from foo_module.bbsort import sorter
import pytest

def test_sorter_empty():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_empty:sorter:0')

def test_sorter_single_element():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([42])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_single_element:sorter:0')
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter(['a'])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_single_element:sorter:1')

def test_sorter_already_sorted():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([1, 2, 3, 4, 5])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_already_sorted:sorter:0')
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter(['a', 'b', 'c'])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_already_sorted:sorter:1')

def test_sorter_all_identical():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([2, 2, 2, 2])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_all_identical:sorter:0')
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter(['x', 'x', 'x'])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_all_identical:sorter:1')

def test_sorter_needs_sorting():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([3, 1, 4, 1, 5, 9, 2, 6, 5])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_needs_sorting:sorter:0')
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter(['b', 'd', 'a', 'c'])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_needs_sorting:sorter:1')

def test_sorter_negative_numbers():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([-3, 0, -1, 5, -2])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_negative_numbers:sorter:0')

def test_sorter_with_duplicates():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([5, 3, 3, 2, 4, 5])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_with_duplicates:sorter:0')

def test_sorter_large_list():
    large_list = [i for i in range(1000, 0, -1)]
    sorted_large_list = sorted(large_list)
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter(large_list)
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_large_list:sorter:2')

def test_sorter_floating_point():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([3.14, 2.71, 1.41, 1.73])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_floating_point:sorter:0')

def test_sorter_special_values():
    gc.disable()
    counter = time.perf_counter_ns()
    return_value = sorter([1, float('inf'), 3, float('-inf')])
    duration = time.perf_counter_ns() - counter
    gc.enable()
    _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_special_values:sorter:0')

def test_sorter_non_list_input():
    with pytest.raises(TypeError):
        gc.disable()
        counter = time.perf_counter_ns()
        return_value = sorter(42)
        duration = time.perf_counter_ns() - counter
        gc.enable()
        _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_non_list_input:sorter:0_0')
    with pytest.raises(TypeError):
        gc.disable()
        counter = time.perf_counter_ns()
        return_value = sorter('string')
        duration = time.perf_counter_ns() - counter
        gc.enable()
        _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_non_list_input:sorter:1_0')
    with pytest.raises(TypeError):
        gc.disable()
        counter = time.perf_counter_ns()
        return_value = sorter({1: 'a', 2: 'b'})
        duration = time.perf_counter_ns() - counter
        gc.enable()
        _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_non_list_input:sorter:2_0')

def test_sorter_various_data_types():
    with pytest.raises(TypeError):
        gc.disable()
        counter = time.perf_counter_ns()
        return_value = sorter([3, 'a', None])
        duration = time.perf_counter_ns() - counter
        gc.enable()
        _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_various_data_types:sorter:0_0')
    with pytest.raises(TypeError):
        gc.disable()
        counter = time.perf_counter_ns()
        return_value = sorter([True, 1, '1'])
        duration = time.perf_counter_ns() - counter
        gc.enable()
        _log__test__values(return_value, duration, 'tests.test_sorter__unit_test_0:test_sorter_various_data_types:sorter:1_0')