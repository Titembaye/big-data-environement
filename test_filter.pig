-- test.pig
data = LOAD '/home/pig/sales.csv' USING PigStorage(',') AS (TransactionID:chararray, CustomerID:chararray, Amount:double, Date:chararray);
high_value_sales = FILTER data BY Amount > 1000;
STORE high_value_sales INTO '/home/pig/high_value_sales' USING PigStorage(',');
