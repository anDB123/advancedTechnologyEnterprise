import pandas as pd
from matplotlib import pyplot as plt


def find_all_ratios(company_name):
    balance_db = pd.read_csv("C:/Users/AndyPC/Desktop/ratioData/{}-balance-sheet.csv".format(company_name),
                             index_col=False, header=1)
    income_db = pd.read_csv("C:/Users/AndyPC/Desktop/ratioData/{}-income-statement.csv".format(company_name),
                            index_col=False, header=1)

    cash_on_hand = balance_db["cash_on_hand"].to_numpy()
    year = [float(x.split('-')[0]) for x in balance_db["field_name"].to_numpy()]

    pre_tax_income = income_db["pre_tax_income"].to_numpy()
    gross_profit = income_db["gross_profit"].to_numpy()
    revenue = income_db["revenue"].to_numpy()
    research_and_development_expenses = income_db["research_and_development_expenses"].to_numpy()
    sg_and_a_expenses = income_db["sg_and_a_expenses"].to_numpy()
    shares_outstanding = income_db["shares_outstanding"].to_numpy()

    cash_on_hand = balance_db["cash_on_hand"].to_numpy()
    receivables = balance_db["receivables"].to_numpy()
    total_current_assets = balance_db["total_current_assets"].to_numpy()
    total_long_term_assets = balance_db["total_long_term_assets"].to_numpy()
    total_current_liabilities = balance_db["total_current_liabilities"].to_numpy()
    total_liabilities = balance_db["total_liabilities"].to_numpy()
    share_holder_equity = balance_db["share_holder_equity"].to_numpy()
    total_long_term_liabilities = balance_db["total_long_term_liabilities"].to_numpy()
    property_and_plant_and_and_equipment = balance_db["property_and_plant_and_and_equipment"].to_numpy()

    # constants
    capital_employed = total_long_term_assets + total_current_assets - total_current_liabilities

    # ratios
    return_on_capital_invested = pre_tax_income / capital_employed
    return_on_shareholder_capital = pre_tax_income / share_holder_equity
    net_profit_margin = pre_tax_income / revenue
    gross_profit_margin = gross_profit / revenue
    current_ratio = total_current_assets / total_current_liabilities
    quick_ratio = (cash_on_hand + receivables) / total_current_liabilities
    # interest_cover = pre_tax_income / interest_expence
    gearing = total_long_term_liabilities / (
            shares_outstanding + total_current_assets + property_and_plant_and_and_equipment)
    return_on_research_spend = gross_profit / research_and_development_expenses

    return [year, return_on_capital_invested, return_on_shareholder_capital, net_profit_margin, gross_profit_margin,
            current_ratio, quick_ratio, gearing, return_on_research_spend]


tesla_ratios = find_all_ratios("tesla")
ford_ratios = find_all_ratios("ford-motor")
toyota_ratios = find_all_ratios("toyota")

variable_names = [
    "year",
    "Return on capital employed (ROCE)",
    "return_on_shareholder_capital",
    "net_profit_margin",
    "gross_profit_margin",
    "current_ratio",
    "quick_ratio",
    "gearing",
    "return_on_research_spend",
]


def plot_ratio_over_time(years, ratios_array, variable_label, labels):
    fig, ax = plt.subplots()
    width = 0.3
    for ratios, label, i in zip(ratios_array, labels, range(len(labels))):
        years_offset = []
        for year in years:
            years_offset.append(year + i * width)
        ax.bar(years_offset, ratios, width=width)
    plt.xticks(rotation=30, ha='right', rotation_mode='anchor')
    ax.set_ylabel(variable_label)
    ax.set_xlabel("Year")
    ax.grid()
    ax.legend(labels)
    plt.show()


for i in range(1, len(tesla_ratios) - 1):
    plot_ratio_over_time(tesla_ratios[0], [tesla_ratios[i], ford_ratios[i], toyota_ratios[i]], variable_names[i],
                         labels=["Tesla", "Ford", "Toyota"])
