#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

# Global Constants
FEDERAL_SALES_TAX = 0.05    # 5%
PROVINCIAL_SALES_TAX = 0.025    # 2.5%

def bill_of_sale(purchase):
    file_name = "Bill of sale.txt"
    with open(file_name, "w") as file_writer:
        write_bill_details_in_file(file_writer,purchase)

def write_bill_details_in_file(file_writer, purchase):
    file_writer.write ("Amount of purchase: {0:.2f}\n".format(purchase))
    file_writer.write ("Provincial tax: {0:.2f}\n".format(purchase * FEDERAL_SALES_TAX))
    file_writer.write ("Federal tax: {0:.2f}\n".format(purchase * PROVINCIAL_SALES_TAX))
    total_tax = FEDERAL_SALES_TAX + PROVINCIAL_SALES_TAX
    file_writer.write ("Total tax: {0:.2f}\n".format(purchase * total_tax))
    file_writer.write ("Total sale: {0:.2f}\n".format(purchase * (1 + total_tax)))

bill_of_sale(100.00)