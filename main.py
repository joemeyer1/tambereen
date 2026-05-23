
#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


from src.scripts.run_tambereen import run_tambereen  # train with standard epochs, standard data
# from tests.test_tambereen import test_tambereen  # train with few epochs, little data
# from tests.test_interact_from_pretrained import test_interact_from_pretrained
# from tests.run_all_tests import run_all_tests




def main():
    return run_tambereen()  # train new tambereen model (standard epochs, standard data)
    # return test_tambereen()  # train new tambereen model (few epochs, little data)
    # return test_interact_from_pretrained(model_dir_path='output_data_runs/28')    
    # return run_all_tests()


if __name__ == '__main__':
    main()
