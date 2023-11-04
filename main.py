from util import generate_dataset
from cbis import calculate_cbis_performance
from rqs import calculate_rqs_performance

if __name__ == '__main__':
    generate_dataset()
    calculate_cbis_performance()
    calculate_rqs_performance()