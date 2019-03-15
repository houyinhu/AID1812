#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs=['iphone case','robot pendangt','dodecahedron']
completed_models=[]
#模拟打印每个设计，直到没有来打印的设计为止
#打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model:"+current_design)
    completed_models.append(current_design)
#显示打印好的所有模型
print("\nThe follwing models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs,completed_models):
    #模拟打印每个设计，直到没有来打印的设计为止
    #打印每个设计后，都将其移到列表completed_designs.pop()
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print("printing model:"+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    #显示打印好的所有模型
    print("\nThe following models haves have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
#print_models(unprinted_designs[:],completed_models)#创建unprinted_designs副本，不改变原列表
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)


