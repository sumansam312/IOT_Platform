from django.contrib import admin
from django.urls import path
from web.views import home_page
from ckt.views import (
    CircuitControlView,
    CircuitStatusView,
    write_api_view,
    read_api_view,
    to_circuit,
    plot_graph,
    chartview,
    graph_two,
    
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page, name="home"),
    path("circuit/", CircuitControlView.as_view(), name="ckt"),
    path("circuit_status/", CircuitStatusView.as_view(), name="ckt_status"),
    path("control/", to_circuit, name="control"),
    path("api_write/", write_api_view, name="write_api"),
    path("api_read/", read_api_view, name="read_api"),
    path("graph_plot/", plot_graph, name="plot_graph"),
    path("chartview/", chartview, name="viewchart"),
    path("graph_two/", graph_two, name="chartview_two"),
    
]
