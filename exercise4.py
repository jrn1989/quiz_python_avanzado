import asyncio

import aiofiles

from io import StringIO

import csv

 

async def read_and_sum_csv(file_name):

    # Read the CSV file content asynchronously

    async with aiofiles.open(file_name, mode='r') as file:

        content = await file.read()

    # Use the csv module to read the content

    reader = csv.DictReader(StringIO(content))

    value_sum = sum(float(row["value"]) for row in reader if "value" in row)

 

    return file_name, value_sum

 

async def async_csv_sum(file_list):

    # Create tasks to read and sum each file asynchronously

    tasks = [read_and_sum_csv(file) for file in file_list]

    # Gather results

    results = await asyncio.gather(*tasks)


    # Create a dictionary from the results

    result_dict = {file_name: value_sum for file_name, value_sum in results}

 

    return result_dict