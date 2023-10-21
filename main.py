from roboflow import Roboflow
rf = Roboflow(api_key="UuIfC3Pbl4KjTg2y5Ldn")
project = rf.workspace("dainius").project("smdcomponents")
dataset = project.version(6).download("yolov8")
