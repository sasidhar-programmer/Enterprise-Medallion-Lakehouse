# Databricks notebook source
# 6. Z-Order Optimization for Downstream Speed

TARGET_TABLE = "tpcds_enterprise.silver.store_sales"

spark.sql(f"""
    OPTIMIZE {TARGET_TABLE}
    ZORDER BY (ss_item_sk, ss_customer_sk)
""")