import torch
data_features = torch.tensor([[1., -1.], [1., -1.]])
if torch.isnan(data_features).any():
  print("data_features tensor has at least one nan value")
