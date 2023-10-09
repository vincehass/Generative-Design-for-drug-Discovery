import hydra
from src.config import GALDConfig

from hydra.core.config_store import ConfigStore
from clamp_common_eval.defaults import get_default_data_splits
import pickle
from omegaconf import DictConfig, OmegaConf
import pandas as pd
import gzip
cs = ConfigStore.instance()
cs.store(name="gald_config", node=GALDConfig)
import os
import random
#from config import get_evalulate_fn, instantiate
import sys


@hydra.main(version_base=None, config_path="./src/conf/", config_name="config")
def main(cfg: GALDConfig)-> None:

    print(OmegaConf.to_yaml(cfg))
    
 

    
    cwd = os.getcwd()
    print(cwd)
    
    cfg.params.seed
    print(f"\nLogging directory of this run:  {cwd}\n")
    # Reset seed for job-name generation in multirun jobs
    # Set other random seeds
    # Configure device count to avoid deserialise error
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    # print(
    #     "\n \tUser-Defined Warning: Oracles must be in increasing order of fidelity. \n \t Best oracle should be the last one in the config list."
    # )
    
    




    logger = hydra.utils.instantiate(cfg.logger, cfg, _recursive_=False)
    


    env = hydra.utils.instantiate(cfg.logger, 
                                  cfg,
                                  _recursive_=False,
                                  device = cfg.params.device,
                                  oracle = cfg.oracles,
                                  train_datset = cfg.datasets.train_data1,
                                  test_data = cfg.datasets.test_data,
                                  negative_ratio = cfg.params.Neg_ratio,
                                  model = cfg.model,
                                  split_method = cfg.datasets.split
                                  )
    
    
    train_data = ["D1", "D2", "D1-177"]
    results = {"Environement setup": env}
    print(results)

    print(cfg.paths.data_result+"/"+str(cfg.datasets.train_data2))


    

    
    for i_dta in train_data:
        data = get_default_data_splits(setting=cfg.datasets.split)# or get_default_data_splits(setting='Title/Target')
        train_data = data.sample(dataset = cfg.datasets.train_data1, neg_ratio = cfg.params.Neg_ratio_eq)
        name_gen_dta = cfg.paths.data_result+"/"+str(i_dta)+"_train.pkl"
        pickle.dump(train_data, open(name_gen_dta, "wb")) 

        gen_file = os.path.abspath(name_gen_dta)
        
        print(gen_file)

        
        # with open(gen_file, "rb") as handle:
        #     b = pickle.load(handle)
        #     print((b))

    return



if __name__ == "__main__":
    main()
    