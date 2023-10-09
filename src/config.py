from dataclasses import dataclass
from collections import OrderedDict
import torch

from omegaconf import DictConfig
from hydra.utils import instantiate

@dataclass
class Paths:
    log:str
    data:str
    data_result: str

@dataclass
class logger:
    project_name:str
  


@dataclass
class Files:
    train_data_d1:str
    train_data_d2:str
    train_data_ALB:str


@dataclass
class Params:  
    Neg_ratio_eq:int
    Neg_ratio:int
    seed:int
    device: str

@dataclass
class Datasets:
    train_data1: str
    train_data2: str
    train_data3: str
    train_data177: str
    split:str #["cluster", "title","target"]

@dataclass
class Oracles:
    D1Target_Albert:str
    D1Target_Albert:str
    D1Target_T5:str
    D2Target_T5:str
    model_mlp:str
    model_RF:str
    method_Albert:str
    method_T5:str


@dataclass
class GALDConfig:
    
    paths: Paths
    files: Files
    params: Params
    datasets:Datasets
    oracles:Oracles
    logger:logger

    