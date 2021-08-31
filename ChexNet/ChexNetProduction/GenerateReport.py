# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:46:52 2021

@author: Andres
"""
from GenerateReportUtils import generate_pdftemplate,get_pdfreport , generate_pdftemplate,generate_predictedlabels

# patient_name = "Prueba 1"
# ID = '102234'
# genre = 'F'
# date = '02/02/02'
# study_name = 'CHEST CT'
# study_date = '01/01/01'

# report='This report was automaticly generated by theStella services. At least one patology pattern was indentified in this study. The heatmap overlead on the image represeted the area with the AI considered to do the automatic evaluation.'
# report = report +report

class GenerateReportClass:
    
  def __init__(self, patient_name, ID, genre,date,study_name,study_date,report,predictions,region):
    self.patient_name = patient_name
    self.ID = ID
    self.genre = genre
    self.date = date
    self.study_name = study_name
    self.study_date = study_date
    self.report = report
    self.predictions = predictions
    self.region = region

  def generate_pdf(self):
      
    predictedlabels=generate_predictedlabels(self.predictions)
    
    generate_pdftemplate(self.patient_name,
                         self.ID,
                         self.genre,
                         self.date,
                         self.study_name,
                         self.study_date,
                         self.report,
                         predictedlabels
                         )
    
    get_pdfreport(self.region)
    
    return

    
    
# GenerateReport('pepito', ID, genre,date,study_name,study_date,report,prediction,'US').generate_pdf()
