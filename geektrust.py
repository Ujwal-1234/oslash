from sys import argv
import json


# functions 
def _apply_disc(price, qty, disc):
    total = 0
    for i in range(0, len(price)):
        total = total + (price[i]*(100-disc[i])/100)*qty[i]
    return total
def _purchase_amount(price, qty):
    total = 0
    for i in range(0, len(price)):
        total = total + price[i]*qty[i]
    return total
def _check(_data):
    meta_data = [
    {
        "product":"TSHIRT",
        "org_price":"1000",
        "discount":"10",
        "category":"clothing"
    },
    {
        "product":"JACKET",
        "org_price":"2000",
        "discount":"5",
        "category":"clothing"
    },
    {
        "product":"CAP",
        "org_price":"500",
        "discount":"20",
        "category":"clothing"
    },
    {
        "product":"NOTEBOOK",
        "org_price":"200",
        "discount":"20",
        "category":"stationary"
    },
    {
        "product":"NOTEBOOK",
        "org_price":"200",
        "discount":"20"
    },
    {
        "product":"PENS",
        "org_price":"300",
        "discount":"10",
        "category":"stationary"
    
    },
    {
        "product":"MARKERS",
        "org_price":"500",
        "discount":"5",
        "category":"stationary"
    
    }
]
    for i in range(0, len(meta_data)):
        if _data == meta_data[i]["product"]:
            return {"price":meta_data[i]["org_price"],"disc":meta_data[i]["discount"],"category":meta_data[i]["category"]}




def main():
    # Sample code to read inputs from the file
    _cloth, _stat = 2, 3
    qty = []
    price = []
    disc = []
    _applied_disc=0
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        line_data = line.split()
        if line_data[0]=="ADD_ITEM":
            _recdata = _check(line_data[1])
            if _recdata["category"] == "clothing":
                if _cloth < int(line_data[2]):
                    print("ERROR_QUANTITY_EXCEEDED")
                    continue
                # _cloth-=int(line_data[2])
                print ("ITEM_ADDED")
                # print (_cloth)
                price.append(int(_recdata["price"]))
                disc.append(int(_recdata["disc"]))
                qty.append(int(line_data[2]))
                
            if _recdata["category"] == "stationary":
                if _stat < int(line_data[2]):
                    print("ERROR_QUANTITY_EXCEEDED")
                    continue
                # _stat-=int(line_data[2])
                print ("ITEM_ADDED")
                price.append(int(_recdata["price"]))
                disc.append(int(_recdata["disc"]))
                qty.append(int(line_data[2])) 
        if line_data[0] == "PRINT_BILL":
            # print(price, qty, disc)
            _purchaseamount = _purchase_amount(price, qty)
            if _purchaseamount > 1000:
                _disc_price = _apply_disc(price, qty, disc)
                _applied_disc = _purchaseamount-_disc_price
                if _disc_price > 3000:
                    _disc_price = round(_disc_price*0.95, 2)
                    _applied_disc = _purchaseamount - _disc_price

            else:
                _disc_price = _purchaseamount
                    # print(_recdata)
            _price_to_pay = _disc_price + _disc_price*0.1
            #   apply tax 10%

            print("TOTAL_DISCOUNT {:0.2f}".format(_applied_disc))
            print("TOTAL_AMOUNT_TO_PAY {:0.2f}".format(_price_to_pay))
            f.close()
            quit()
    
    
if __name__ == "__main__":
    main()