from pyes import ES
from pyes import TermQuery
from pyes import RangeQuery
from pyes import QueryStringQuery
from pyes import BoolQuery
from pyes import ESRange
from pyes import ANDFilter
from pyes import TermFilter
from pyes import FilteredQuery
from pyes import query

conn = ES('localhost:9200')

a_range = RangeQuery(qrange=ESRange('a', 0.179, 0.180))
b_filter = TermFilter("b", "0.2")
period_filter = TermFilter("period", "2")
total_filter = ANDFilter([b_filter, period_filter])
c_range = RangeQuery(qrange=ESRange('c', 8, 12))
que = FilteredQuery(BoolQuery(must=[a_range, c_range]), total_filter)

search = query.Search(query=que)
get = conn.search(search, indices='shrimp')
census =get.total

for i in get:
   print i
