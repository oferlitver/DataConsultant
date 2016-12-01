#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Experiment class
@author: ofer
"""
import configparser
import unittest


class Experiment():
    
    def __init__(self, experiment_condition, config_file='./config/config.ini'):
        """ The class gets an experiment condition and reads values from the
        appropriate section in the config file
        
        experiment_condition : string
        
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)


class TestExperiment(unittest.TestCase):
    
    def test_reading(self):
        experiment = Experiment('condition1')
#        self.assertEqual(experiment.config['numsites'], 4)
        self.assertEqual(experiment.config.getint('condition1', 'numsites'), 4)
        

if __name__ == '__main__':
    unittest.main()
    
