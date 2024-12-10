import pytest
import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_login_excersice7/SRC')
import DB.model as model

@pytest.mark.parametrize(
        """id,productName,quantity""",
        [
            (1,"Offset paper",100),
            (2,"Bond paper",110),
            (3,"Coasted paper",105)
        ]
)
def test_kind_of_products(id,productName,quantity):
    
    product_test=model.Product(id,productName,quantity)
    assert (product_test.IDPRODUCTS,product_test.PRODUCTNAME,product_test.PRODUCTPRICE)==(id,productName,quantity)

@pytest.mark.parametrize(
        """id,name,lastName,email""",
        [
            (41,"Regina Arias","Lee","ReginaArias@gmail.com"),
            (42,"Brenda Lopez","Lopez","BrendaLopez@gmail.com"),
            (43,"Chelsey Taylor",",Mathis","amber51@example.org")
        ]
)
def test_kind_of_sellers(id,name,lastName,email):
    seller_test=model.Seller(id,name,lastName,email)
    assert (seller_test.IDSELLER,seller_test.NAME,seller_test.LASTNAME,seller_test.EMAILADRESS)==(id,name,lastName,email)

@pytest.mark.parametrize(
        """idsell,idproducts,idseller,quantity""",
        [
            (41,23,53,6),
            (42,24,43,9),
            (43,21,43,9)
        ]
)
def test_kind_of_sells(idsell,idproducts,idseller,quantity):
    sell_test=model.Sell(idsell,idproducts,idseller,quantity)
    assert (sell_test.IDSELLS,sell_test.IDPRODUCTS,sell_test.IDSELLER,sell_test.QUANTITY)==(idsell,idproducts,idseller,quantity)

@pytest.mark.parametrize(
        """idbatch,idproduct,quantity""",
        [
            (1,1,50),
            (2,2,110),
            (3,3,105)
        ]
)
def test_kind_of_batch(idbatch,idproduct,quantity):
    batch_test=model.Batch(idbatch,idproduct,quantity)
    assert (batch_test.IDBATCH,batch_test.IDPRODUCTS,batch_test._PURCHARSED_QUANTITY)==(idbatch,idproduct,quantity)