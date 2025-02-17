import ibis
from taipy import Gui

t=ibis.read_csv("bronx_restaurant_inspections.csv")
data=t.to_pandas()
restaurant = ""
t_restaurant= t.select("DBA").order_by("DBA").distinct().execute()
restaurant_list = t_restaurant["DBA"].tolist()
rdata=t.filter(t["DBA"]=="No Such Restaurant").to_pandas()

def change_restaurant(state):
    name = state.restaurant 
    state.rdata = t.filter(t["DBA"] == name).to_pandas()
    
page1="""
<|navbar|>
# Bronx Restaurant Inspections
<|{data}|table|>
"""

page2="""
<|navbar|>
# Select a restaurant
<|{restaurant}|selector|lov={restaurant_list}|dropdown|on_change=change_restaurant|>
<|{rdata}|table|>
"""


pages={
	"Data":page1,
	"Charts":page2
}

Gui(pages=pages).run(port="auto", use_reloader=True)


