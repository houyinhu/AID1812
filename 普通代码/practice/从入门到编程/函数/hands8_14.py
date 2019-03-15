

def make_car(seller,model,**args):
    d={}
    d['seller']=seller
    d['model']=model

    for key,value in args.items():
        d[key]=value
    return d
car=make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)



