import pytest
import sys
sys.path.append('C:/Users/ferna/Documents/Flask_projects/Flask_login_excersice7/SRC')
import DB.model as model
import pytest
from datetime import timedelta,date

today=date.today()
tomorrow=today+timedelta(days=1)
later=tomorrow+timedelta(days=10)

@pytest.mark.parametrize(
        "id,idProduct,idSeller,Quantity_batch,Quantity_sell",
        [
            (1,2,100,100,20),
            (1,1112,10,5,5),
            (3,8,10,500,50)
        ]
)
def test_can_be_allocation_sell_less_quantity_than_batch_available(id,idProduct,idSeller,Quantity_batch,Quantity_sell):
    batch_test=model.Batch(id,idProduct,Quantity_batch,None)
    sell_test=model.Sell(id,idProduct,idSeller,Quantity_sell)
    batch_test.can_allocate(sell_test)

    assert batch_test.can_allocate(sell_test)==True

@pytest.mark.parametrize(
        "id1,id2,id3,idProduct,Quantity,eta1,eta2,eta3",
        [
            (10,20,30,3,100,today,tomorrow,later),
            (20,10,30,4,100,today,tomorrow,later),
            (30,10,20,5,100,today,tomorrow,later),
            (40,50,60,1,10,today,tomorrow,later),
            (50,40,60,1,30,today,tomorrow,later),
            (60,50,60,1,2,today,tomorrow,later),

        ]
)
def test_allocation_sorted(id1,id2,id3,idProduct,Quantity,eta1,eta2,eta3):
    """Test the method __gt__"""
    batch_test_today=model.Batch(id1,idProduct,Quantity,eta1)
    batch_test_tomorrow=model.Batch(id2,idProduct,Quantity,eta2)
    batch_test_latter=model.Batch(id3,idProduct,Quantity,eta3)

    assert sorted([batch_test_tomorrow,batch_test_today,batch_test_latter])==[batch_test_today,batch_test_tomorrow,batch_test_latter]
    