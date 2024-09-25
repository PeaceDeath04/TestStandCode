key_to_Graphs = {
            "TractionGraph": {"x": "Time", "y": "Traction"},
            "WeightGraph": {"x": "Time", "y": "mainWeight"}
        }
graphs ={}
graphs = key_to_Graphs.copy()
key_to_Graphs["TractionGraph"]["z"] = 3

for nameGraph, params in graphs.items():
    graphs[nameGraph].get()
