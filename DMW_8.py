{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNhtIc1H+KhXhLWJP/nEUfS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/Bhushan-14/Python/blob/main/DMW_8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = [\n",
        "    ['T100', ['11', '12','15']],\n",
        "    ['T200', ['12', '14']],\n",
        "    ['T300', ['12','13']],\n",
        "    ['T400', ['11', '12', '14']],\n",
        "    ['T500', ['11', '13']],\n",
        "    ['T600', ['12','13']],\n",
        "    ['T700', ['11', '13']],\n",
        "    ['1800', ['11', '12', '13', '15']],\n",
        "    ['T900', ['11', '12', '13']]\n",
        "    ]"
      ],
      "metadata": {
        "id": "hKjn8MX6ZMIe"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "init = []\n",
        "for i in data:\n",
        "  for q in i[1]:\n",
        "    if(q not in init):\n",
        "      init.append(q)\n",
        "init = sorted(init)\n",
        "print(init)\n",
        "sp = 0.4\n",
        "s = int(sp*len(init))\n",
        "print('------------------------------')\n",
        "print(s)"
      ],
      "metadata": {
        "id": "agGeD6PFZf5J",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "outputId": "b1fe34e8-e878-4037-b6a8-a3e5de62edca"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['11', '12', '13', '14', '15']\n",
            "------------------------------\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from collections import Counter\n",
        "c = Counter()\n",
        "for i in init:\n",
        "  for d in data:\n",
        "    if(i in d[1]) :\n",
        "        c[i]+=1\n",
        "print(\"C1:\")\n",
        "for i in c:\n",
        "  print(str ([i])+\": \"+str(c[i]))\n",
        "print()\n",
        "l = Counter()\n",
        "for i in c:\n",
        "  if(c[i]>=s) :\n",
        "    l[frozenset([i])] +=c[i]"
      ],
      "metadata": {
        "id": "kcSo2aoHZ1ZR",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "outputId": "8c41bb38-13c3-4695-f44c-c5d0ae77e664"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "C1:\n",
            "['11']: 6\n",
            "['12']: 7\n",
            "['13']: 6\n",
            "['14']: 2\n",
            "['15']: 2\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"L1:\")\n",
        "for i in l:\n",
        "    print(str(list(i)) + \": \" + str(l[i]))\n",
        "print()\n",
        "\n",
        "pl = l\n",
        "pos = 1\n",
        "\n",
        "for count in range(2, 1000):\n",
        "    nc = set()\n",
        "    temp = list(l)\n",
        "\n",
        "    for i in range(0, len(temp)):\n",
        "        for j in range(i + 1, len(temp)):\n",
        "            t = temp[i].union(temp[j])\n",
        "            if len(t) == count:\n",
        "                nc.add(temp[i].union(temp[j]))\n",
        "    nc = list(nc)\n",
        "    c = Counter()\n",
        "    for i in nc:\n",
        "        c[i] = 0\n",
        "        for q in data:\n",
        "            temp = set(q[1])\n",
        "            if i.issubset(temp):\n",
        "                c[i] += 1\n",
        "\n",
        "    print(\"C\" + str(count) + \":\")\n",
        "    for i in c:\n",
        "        print(str(list(i)) + \": \" + str(c[i]))\n",
        "    print()\n",
        "\n",
        "    l = Counter()\n",
        "    for i in c:\n",
        "        if c[i] >= s:\n",
        "            l[i] += c[i]\n",
        "\n",
        "    print(\"L\" + str(count) + \":\")\n",
        "    for i in l:\n",
        "        print(str(list(i)) + \": \" + str(l[i]))\n",
        "    print()\n",
        "\n",
        "    if len(l) == 0:\n",
        "        break\n",
        "    pl = l\n",
        "    pos = count\n",
        "\n",
        "print(\"Final Result:\")\n",
        "print(\"L\" + str(pos) + \":\")\n",
        "for i in pl:\n",
        "    print(str(i) + \": \" + str(pl[i]))"
      ],
      "metadata": {
        "id": "AxiMyjKUabSp",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "outputId": "026e7bae-7dc7-4663-e3de-c1e865a89339"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "L1:\n",
            "['11']: 6\n",
            "['12']: 7\n",
            "['13']: 6\n",
            "['14']: 2\n",
            "['15']: 2\n",
            "\n",
            "C2:\n",
            "['11', '14']: 1\n",
            "['11', '12']: 4\n",
            "['11', '13']: 4\n",
            "['14', '15']: 0\n",
            "['12', '15']: 2\n",
            "['14', '13']: 0\n",
            "['15', '13']: 1\n",
            "['12', '14']: 2\n",
            "['11', '15']: 2\n",
            "['12', '13']: 4\n",
            "\n",
            "L2:\n",
            "['11', '12']: 4\n",
            "['11', '13']: 4\n",
            "['12', '15']: 2\n",
            "['12', '14']: 2\n",
            "['11', '15']: 2\n",
            "['12', '13']: 4\n",
            "\n",
            "C3:\n",
            "['11', '12', '15']: 2\n",
            "['11', '12', '14']: 1\n",
            "['11', '15', '13']: 1\n",
            "['11', '12', '13']: 2\n",
            "['12', '13', '14']: 0\n",
            "['12', '15', '14']: 0\n",
            "['12', '15', '13']: 1\n",
            "\n",
            "L3:\n",
            "['11', '12', '15']: 2\n",
            "['11', '12', '13']: 2\n",
            "\n",
            "C4:\n",
            "['15', '11', '12', '13']: 1\n",
            "\n",
            "L4:\n",
            "\n",
            "Final Result:\n",
            "L3:\n",
            "frozenset({'11', '12', '15'}): 2\n",
            "frozenset({'11', '12', '13'}): 2\n"
          ]
        }
      ]
    }
  ]
}