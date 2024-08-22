import os
import pandas as pd


class Calculation:  # singleton design pattern

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Calculation, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):  # To avoid reinitialization
            self.initialized = True
            file_path = os.getenv("FILEPATH")  # get enviromental variable csv file path
            self.df = pd.read_csv(file_path)  # read csv

    def conversion_rate(self) -> dict:

        conversion_df = self.df.copy(deep=True)  # create deep copy of dataframe

        grouped_df = (
            conversion_df.groupby("customer_id")
            .agg({"revenue": "sum", "conversions": "sum"})
            .reset_index()
        )  # Group by customer and calculate totals"

        grouped_df["conversion_rate"] = (
            grouped_df["conversions"] / grouped_df["revenue"]
        )  # conversion rate calculation conversion/revenue

        # Identify the customer_ids with the highest and lowest conversion rates.
        highest_conversion_rate = grouped_df.loc[grouped_df["conversion_rate"].idxmax()]
        lowest_conversion_rate = grouped_df.loc[grouped_df["conversion_rate"].idxmin()]

        # converst dict
        conversion_rate = grouped_df[["customer_id", "conversion_rate"]].to_dict(
            orient="records"
        )
        highest_conversion = highest_conversion_rate[
            ["customer_id", "conversion_rate"]
        ].to_dict()
        lowest_conversion = lowest_conversion_rate[
            ["customer_id", "conversion_rate"]
        ].to_dict()

        return {
            "conversion_rate": conversion_rate,
            "highest_conversion": highest_conversion,
            "lowest_conversion": lowest_conversion,
        }

    def status_based(self) -> dict:

        status_based_df = self.df.copy(deep=True)  # create deep copy of dataframe

        status_distribution = (
            status_based_df.groupby(["type", "category", "status"])
            .size()
            .unstack(fill_value=0)
        )

        status_totals = status_based_df.groupby("status").agg(
            {"revenue": "sum", "conversions": "sum"}
        )

        # convert dict
        distribution = status_distribution.reset_index().to_dict(orient="records")
        totals = status_totals.to_dict(orient="records")

        return {"distribution": distribution, "totals": totals}

    def category_type_performance(self):
        performance_df = self.df.copy(deep=True)  # create deep copy of dataframe

        performance = performance_df.groupby(["category", "type"]).agg(
            {"revenue": "sum", "conversions": "sum"}
        )  # Calculation of total revenue and total conversion

        max_conversions = performance["conversions"].idxmax()
        max_conversions_value = performance["conversions"].max()

        # bakılacak
        # convert dict
        performance_dict = performance.reset_index().to_dict(orient="records")
        # max_conversions_dict=max_conversions
        return {
            "performance": performance_dict,
            "max_conversions": list(max_conversions),
            "max_conversions_value": max_conversions_value,
        }

    def filter_and_aggregate(self):  # bakılacak
        filter_df = self.df.copy(deep=True)  # create deep copy of dataframe

        # filter conversion rows
        filtered_df = filter_df[filter_df["type"] == "CONVERSION"]

        # aggreate and get average
        aggregated_df = (
            filtered_df.groupby("customer_id")
            .agg({"revenue": "mean", "conversions": "mean"})
            .reset_index()
        )

        # convert dict
        filtered_dict = filtered_df.to_dict(orient="records")
        aggregated_dict = aggregated_df.to_dict(orient="records")
        return {
            "conversion_data": filtered_dict,
            "average_performance": aggregated_dict,
        }
