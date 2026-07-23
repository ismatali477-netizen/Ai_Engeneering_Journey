import torch
x = torch.tensor(4.0, requires_grad=True)
y=x**2
z=y+5
print(z.item())
z.backward()
print(x.grad)