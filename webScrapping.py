{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Amazon Reviews - Web Scrapping.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyN0LBKJUaSxNOy24cOhIen6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kavya2905/ML-AI-Basic-Projects/blob/main/Amazon_Reviews_Web_Scrapping.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n5fGt2zX-Yls"
      },
      "source": [
        "### Importing libraries\r\n",
        "\r\n",
        "import requests\r\n",
        "from bs4 import BeautifulSoup\r\n",
        "import pandas as pd"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lsqNIW4g-ZpB"
      },
      "source": [
        "cust_name = []\r\n",
        "cust_rating = []\r\n",
        "rev_date = []\r\n",
        "rev_title = []\r\n",
        "rev_text = []"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vjDNpfmB-e3I"
      },
      "source": [
        "\r\n",
        "for url in range(0,10):\r\n",
        "  url = requests.get(\"https://www.amazon.in/New-Apple-iPhone-11-64GB/product-reviews/B08L8DV7BX/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=\"+str(url))\r\n",
        "  soup = BeautifulSoup(url.content, 'html.parser')\r\n",
        "  names = soup.select('span.a-profile-name')\r\n",
        "  stars = soup.select('span.a-icon-alt')\r\n",
        "  titles = soup.select('a.review-title span')\r\n",
        "  dates = soup.select('span.review-date')[2:]\r\n",
        "  reviews = soup.select('span.review-text span')\r\n",
        "  for i in range(10):\r\n",
        "    cust_name.append(names[i].get_text())\r\n",
        "    cust_rating.append(stars[i].get_text().rstrip(\" out of 5 stars\"))\r\n",
        "    rev_date.append(dates[i].get_text().lstrip(\"Reviewed in India on \"))\r\n",
        "    rev_title.append(titles[i].get_text())\r\n",
        "    rev_text.append(reviews[i].get_text().strip(\"\\n\"))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eA4T6o6E-n24"
      },
      "source": [
        "\r\n",
        "df = pd.DataFrame()\r\n",
        "df['Date'] = rev_date\r\n",
        "df['Customer Name'] = cust_name\r\n",
        "df['Ratings'] = cust_rating\r\n",
        "df['Title'] = rev_title\r\n",
        "df['Reviews'] = rev_text"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        },
        "id": "mmwedBE1-8it",
        "outputId": "02cf058f-85c6-49cb-fd98-1c35384bfe4b"
      },
      "source": [
        "df"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Date</th>\n",
              "      <th>Customer Name</th>\n",
              "      <th>Ratings</th>\n",
              "      <th>Title</th>\n",
              "      <th>Reviews</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>10 July 2020</td>\n",
              "      <td>shanu Kumar</td>\n",
              "      <td>4.</td>\n",
              "      <td>Do not buy iphone or expensive product from Am...</td>\n",
              "      <td>Please do not buy expensive product like iph...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>13 November 2019</td>\n",
              "      <td>Neha</td>\n",
              "      <td>5.0</td>\n",
              "      <td>Don’t buy it from this seller</td>\n",
              "      <td>Bought the mobile from appario retail ltd. M...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>30 September 2019</td>\n",
              "      <td>Neha</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Solid premium phone from Apple</td>\n",
              "      <td>Awesome Phone. Nice upgrade from iPhone 6s t...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>14 October 2019</td>\n",
              "      <td>Krusshna</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Worst Experience Ever.!</td>\n",
              "      <td>My Phone is Producing Too Much Heat Even Did...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>29 September 2019</td>\n",
              "      <td>shanu Kumar</td>\n",
              "      <td>1.0</td>\n",
              "      <td>First Time iPhone User Review :-)</td>\n",
              "      <td>The iPhone design is good and the camera qua...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>135</th>\n",
              "      <td>22 July 2020</td>\n",
              "      <td>Amazon Customer</td>\n",
              "      <td>5.0</td>\n",
              "      <td>GOT CHEATED . ITS A SCAM. AMAZON FIX THIS</td>\n",
              "      <td>This is a big scam. I received the iphone 11...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>136</th>\n",
              "      <td>10 October 2019</td>\n",
              "      <td>Sunny Kumar</td>\n",
              "      <td>1.0</td>\n",
              "      <td>iPhone 11</td>\n",
              "      <td>Defective product,got heat up within 5 minut...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>137</th>\n",
              "      <td>14 October 2019</td>\n",
              "      <td>Sai</td>\n",
              "      <td>5.0</td>\n",
              "      <td>Defective Iphone 11</td>\n",
              "      <td>The product i got was defective . The face i...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>138</th>\n",
              "      <td>21 October 2019</td>\n",
              "      <td>Satyapal singh</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Too much heat on normal use</td>\n",
              "      <td>Just after i switched it on, it started prod...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>139</th>\n",
              "      <td>8 November 2019</td>\n",
              "      <td>Gurmeet singh</td>\n",
              "      <td>1.0</td>\n",
              "      <td>Provided with a defective product</td>\n",
              "      <td>Provided with defective product .Struggling ...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>140 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                  Date  ...                                            Reviews\n",
              "0         10 July 2020  ...    Please do not buy expensive product like iph...\n",
              "1     13 November 2019  ...    Bought the mobile from appario retail ltd. M...\n",
              "2    30 September 2019  ...    Awesome Phone. Nice upgrade from iPhone 6s t...\n",
              "3      14 October 2019  ...    My Phone is Producing Too Much Heat Even Did...\n",
              "4    29 September 2019  ...    The iPhone design is good and the camera qua...\n",
              "..                 ...  ...                                                ...\n",
              "135       22 July 2020  ...    This is a big scam. I received the iphone 11...\n",
              "136    10 October 2019  ...    Defective product,got heat up within 5 minut...\n",
              "137    14 October 2019  ...    The product i got was defective . The face i...\n",
              "138    21 October 2019  ...    Just after i switched it on, it started prod...\n",
              "139    8 November 2019  ...    Provided with defective product .Struggling ...\n",
              "\n",
              "[140 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x-sxakrq-95e"
      },
      "source": [
        "df.to_csv(\"amazon_product_review.csv\")"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
