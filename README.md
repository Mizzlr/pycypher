# Pycypher
A python module to parse cypher query string and generate AST.

## Installation

```bash
$ git clone https://github.com/Mizzlr/pycypher
$ cd pycypher
$ python3 setup.py install
```

## Example
Open python3 interpreter with command `python3` and run the following.

```python
>>> import pycypher
>>> import json
>>> print(json.dumps(pycypher.parse('MATCH (n) RETURN Count(n);'), indent=2))
{
  "result": [
    {
      "node": {
        "parent": "Cypher",
        "text": "",
        "sourceInterval": [
          -1,
          -2
        ]
      },
      "children": {
        "result": [],
        "errors": []
      }
    },
    {
      "node": {
        "parent": "Cypher",
        "text": "MATCH (n) RETURN Count(n)",
        "sourceInterval": [
          0,
          11
        ]
      },
      "children": {
        "result": [
          {
            "node": {
              "parent": "Statement",
              "text": "MATCH (n) RETURN Count(n)",
              "sourceInterval": [
                0,
                11
              ]
            },
            "children": {
              "result": [
                {
                  "node": {
                    "parent": "Query",
                    "text": "MATCH (n) RETURN Count(n)",
                    "sourceInterval": [
                      0,
                      11
                    ]
                  },
                  "children": {
                    "result": [
                      {
                        "node": {
                          "parent": "RegularQuery",
                          "text": "MATCH (n) RETURN Count(n)",
                          "sourceInterval": [
                            0,
                            11
                          ]
                        },
                        "children": {
                          "result": [
                            {
                              "node": {
                                "parent": "SingleQuery",
                                "text": "MATCH (n) RETURN Count(n)",
                                "sourceInterval": [
                                  0,
                                  11
                                ]
                              },
                              "children": {
                                "result": [
                                  {
                                    "node": {
                                      "parent": "SinglePartQuery",
                                      "text": "MATCH (n)",
                                      "sourceInterval": [
                                        0,
                                        4
                                      ]
                                    },
                                    "children": {
                                      "result": [
                                        {
                                          "node": {
                                            "parent": "ReadingClause",
                                            "text": "MATCH (n)",
                                            "sourceInterval": [
                                              0,
                                              4
                                            ]
                                          },
                                          "children": {
                                            "result": [
                                              {
                                                "node": {
                                                  "parent": "Match",
                                                  "text": "MATCH",
                                                  "sourceInterval": [
                                                    0,
                                                    0
                                                  ]
                                                },
                                                "children": {
                                                  "parent": "Match",
                                                  "text": "MATCH",
                                                  "sourceInterval": [
                                                    0,
                                                    0
                                                  ]
                                                }
                                              },
                                              {
                                                "node": {
                                                  "parent": "Match",
                                                  "text": " ",
                                                  "sourceInterval": [
                                                    1,
                                                    1
                                                  ]
                                                },
                                                "children": {
                                                  "parent": "Match",
                                                  "text": " ",
                                                  "sourceInterval": [
                                                    1,
                                                    1
                                                  ]
                                                }
                                              },
                                              {
                                                "node": {
                                                  "parent": "Match",
                                                  "text": "(n)",
                                                  "sourceInterval": [
                                                    2,
                                                    4
                                                  ]
                                                },
                                                "children": {
                                                  "result": [
                                                    {
                                                      "node": {
                                                        "parent": "Pattern",
                                                        "text": "(n)",
                                                        "sourceInterval": [
                                                          2,
                                                          4
                                                        ]
                                                      },
                                                      "children": {
                                                        "result": [
                                                          {
                                                            "node": {
                                                              "parent": "PatternPart",
                                                              "text": "(n)",
                                                              "sourceInterval": [
                                                                2,
                                                                4
                                                              ]
                                                            },
                                                            "children": {
                                                              "result": [
                                                                {
                                                                  "node": {
                                                                    "parent": "AnonymousPatternPart",
                                                                    "text": "(n)",
                                                                    "sourceInterval": [
                                                                      2,
                                                                      4
                                                                    ]
                                                                  },
                                                                  "children": {
                                                                    "result": [
                                                                      {
                                                                        "node": {
                                                                          "parent": "PatternElement",
                                                                          "text": "(n)",
                                                                          "sourceInterval": [
                                                                            2,
                                                                            4
                                                                          ]
                                                                        },
                                                                        "children": {
                                                                          "result": [
                                                                            {
                                                                              "node": {
                                                                                "parent": "NodePattern",
                                                                                "text": "(",
                                                                                "sourceInterval": [
                                                                                  2,
                                                                                  2
                                                                                ]
                                                                              },
                                                                              "children": {
                                                                                "parent": "NodePattern",
                                                                                "text": "(",
                                                                                "sourceInterval": [
                                                                                  2,
                                                                                  2
                                                                                ]
                                                                              }
                                                                            },
                                                                            {
                                                                              "node": {
                                                                                "parent": "NodePattern",
                                                                                "text": "n",
                                                                                "sourceInterval": [
                                                                                  3,
                                                                                  3
                                                                                ]
                                                                              },
                                                                              "children": {
                                                                                "result": [
                                                                                  {
                                                                                    "node": {
                                                                                      "parent": "Variable",
                                                                                      "text": "n",
                                                                                      "sourceInterval": [
                                                                                        3,
                                                                                        3
                                                                                      ]
                                                                                    },
                                                                                    "children": {
                                                                                      "result": [
                                                                                        {
                                                                                          "node": {
                                                                                            "parent": "SymbolicName",
                                                                                            "text": "n",
                                                                                            "sourceInterval": [
                                                                                              3,
                                                                                              3
                                                                                            ]
                                                                                          },
                                                                                          "children": {
                                                                                            "parent": "SymbolicName",
                                                                                            "text": "n",
                                                                                            "sourceInterval": [
                                                                                              3,
                                                                                              3
                                                                                            ]
                                                                                          }
                                                                                        }
                                                                                      ],
                                                                                      "errors": []
                                                                                    }
                                                                                  }
                                                                                ],
                                                                                "errors": []
                                                                              }
                                                                            },
                                                                            {
                                                                              "node": {
                                                                                "parent": "NodePattern",
                                                                                "text": ")",
                                                                                "sourceInterval": [
                                                                                  4,
                                                                                  4
                                                                                ]
                                                                              },
                                                                              "children": {
                                                                                "parent": "NodePattern",
                                                                                "text": ")",
                                                                                "sourceInterval": [
                                                                                  4,
                                                                                  4
                                                                                ]
                                                                              }
                                                                            }
                                                                          ],
                                                                          "errors": []
                                                                        }
                                                                      }
                                                                    ],
                                                                    "errors": []
                                                                  }
                                                                }
                                                              ],
                                                              "errors": []
                                                            }
                                                          }
                                                        ],
                                                        "errors": []
                                                      }
                                                    }
                                                  ],
                                                  "errors": []
                                                }
                                              }
                                            ],
                                            "errors": []
                                          }
                                        }
                                      ],
                                      "errors": []
                                    }
                                  },
                                  {
                                    "node": {
                                      "parent": "SinglePartQuery",
                                      "text": " ",
                                      "sourceInterval": [
                                        5,
                                        5
                                      ]
                                    },
                                    "children": {
                                      "parent": "SinglePartQuery",
                                      "text": " ",
                                      "sourceInterval": [
                                        5,
                                        5
                                      ]
                                    }
                                  },
                                  {
                                    "node": {
                                      "parent": "SinglePartQuery",
                                      "text": "RETURN Count(n)",
                                      "sourceInterval": [
                                        6,
                                        11
                                      ]
                                    },
                                    "children": {
                                      "result": [
                                        {
                                          "node": {
                                            "parent": "Return",
                                            "text": "RETURN",
                                            "sourceInterval": [
                                              6,
                                              6
                                            ]
                                          },
                                          "children": {
                                            "parent": "Return",
                                            "text": "RETURN",
                                            "sourceInterval": [
                                              6,
                                              6
                                            ]
                                          }
                                        },
                                        {
                                          "node": {
                                            "parent": "Return",
                                            "text": " ",
                                            "sourceInterval": [
                                              7,
                                              7
                                            ]
                                          },
                                          "children": {
                                            "parent": "Return",
                                            "text": " ",
                                            "sourceInterval": [
                                              7,
                                              7
                                            ]
                                          }
                                        },
                                        {
                                          "node": {
                                            "parent": "Return",
                                            "text": "Count(n)",
                                            "sourceInterval": [
                                              8,
                                              11
                                            ]
                                          },
                                          "children": {
                                            "result": [
                                              {
                                                "node": {
                                                  "parent": "ReturnBody",
                                                  "text": "Count(n)",
                                                  "sourceInterval": [
                                                    8,
                                                    11
                                                  ]
                                                },
                                                "children": {
                                                  "result": [
                                                    {
                                                      "node": {
                                                        "parent": "ReturnItems",
                                                        "text": "Count(n)",
                                                        "sourceInterval": [
                                                          8,
                                                          11
                                                        ]
                                                      },
                                                      "children": {
                                                        "result": [
                                                          {
                                                            "node": {
                                                              "parent": "ReturnItem",
                                                              "text": "Count(n)",
                                                              "sourceInterval": [
                                                                8,
                                                                11
                                                              ]
                                                            },
                                                            "children": {
                                                              "result": [
                                                                {
                                                                  "node": {
                                                                    "parent": "Expression",
                                                                    "text": "Count(n)",
                                                                    "sourceInterval": [
                                                                      8,
                                                                      11
                                                                    ]
                                                                  },
                                                                  "children": {
                                                                    "result": [
                                                                      {
                                                                        "node": {
                                                                          "parent": "OrExpression",
                                                                          "text": "Count(n)",
                                                                          "sourceInterval": [
                                                                            8,
                                                                            11
                                                                          ]
                                                                        },
                                                                        "children": {
                                                                          "result": [
                                                                            {
                                                                              "node": {
                                                                                "parent": "XorExpression",
                                                                                "text": "Count(n)",
                                                                                "sourceInterval": [
                                                                                  8,
                                                                                  11
                                                                                ]
                                                                              },
                                                                              "children": {
                                                                                "result": [
                                                                                  {
                                                                                    "node": {
                                                                                      "parent": "AndExpression",
                                                                                      "text": "Count(n)",
                                                                                      "sourceInterval": [
                                                                                        8,
                                                                                        11
                                                                                      ]
                                                                                    },
                                                                                    "children": {
                                                                                      "result": [
                                                                                        {
                                                                                          "node": {
                                                                                            "parent": "NotExpression",
                                                                                            "text": "Count(n)",
                                                                                            "sourceInterval": [
                                                                                              8,
                                                                                              11
                                                                                            ]
                                                                                          },
                                                                                          "children": {
                                                                                            "result": [
                                                                                              {
                                                                                                "node": {
                                                                                                  "parent": "ComparisonExpression",
                                                                                                  "text": "Count(n)",
                                                                                                  "sourceInterval": [
                                                                                                    8,
                                                                                                    11
                                                                                                  ]
                                                                                                },
                                                                                                "children": {
                                                                                                  "result": [
                                                                                                    {
                                                                                                      "node": {
                                                                                                        "parent": "AddOrSubtractExpression",
                                                                                                        "text": "Count(n)",
                                                                                                        "sourceInterval": [
                                                                                                          8,
                                                                                                          11
                                                                                                        ]
                                                                                                      },
                                                                                                      "children": {
                                                                                                        "result": [
                                                                                                          {
                                                                                                            "node": {
                                                                                                              "parent": "MultiplyDivideModuloExpression",
                                                                                                              "text": "Count(n)",
                                                                                                              "sourceInterval": [
                                                                                                                8,
                                                                                                                11
                                                                                                              ]
                                                                                                            },
                                                                                                            "children": {
                                                                                                              "result": [
                                                                                                                {
                                                                                                                  "node": {
                                                                                                                    "parent": "PowerOfExpression",
                                                                                                                    "text": "Count(n)",
                                                                                                                    "sourceInterval": [
                                                                                                                      8,
                                                                                                                      11
                                                                                                                    ]
                                                                                                                  },
                                                                                                                  "children": {
                                                                                                                    "result": [
                                                                                                                      {
                                                                                                                        "node": {
                                                                                                                          "parent": "UnaryAddOrSubtractExpression",
                                                                                                                          "text": "Count(n)",
                                                                                                                          "sourceInterval": [
                                                                                                                            8,
                                                                                                                            11
                                                                                                                          ]
                                                                                                                        },
                                                                                                                        "children": {
                                                                                                                          "result": [
                                                                                                                            {
                                                                                                                              "node": {
                                                                                                                                "parent": "StringListNullOperatorExpression",
                                                                                                                                "text": "Count(n)",
                                                                                                                                "sourceInterval": [
                                                                                                                                  8,
                                                                                                                                  11
                                                                                                                                ]
                                                                                                                              },
                                                                                                                              "children": {
                                                                                                                                "result": [
                                                                                                                                  {
                                                                                                                                    "node": {
                                                                                                                                      "parent": "PropertyOrLabelsExpression",
                                                                                                                                      "text": "Count(n)",
                                                                                                                                      "sourceInterval": [
                                                                                                                                        8,
                                                                                                                                        11
                                                                                                                                      ]
                                                                                                                                    },
                                                                                                                                    "children": {
                                                                                                                                      "result": [
                                                                                                                                        {
                                                                                                                                          "node": {
                                                                                                                                            "parent": "Atom",
                                                                                                                                            "text": "Count(n)",
                                                                                                                                            "sourceInterval": [
                                                                                                                                              8,
                                                                                                                                              11
                                                                                                                                            ]
                                                                                                                                          },
                                                                                                                                          "children": {
                                                                                                                                            "result": [
                                                                                                                                              {
                                                                                                                                                "node": {
                                                                                                                                                  "parent": "FunctionInvocation",
                                                                                                                                                  "text": "Count",
                                                                                                                                                  "sourceInterval": [
                                                                                                                                                    8,
                                                                                                                                                    8
                                                                                                                                                  ]
                                                                                                                                                },
                                                                                                                                                "children": {
                                                                                                                                                  "result": [
                                                                                                                                                    {
                                                                                                                                                      "node": {
                                                                                                                                                        "parent": "FunctionName",
                                                                                                                                                        "text": "",
                                                                                                                                                        "sourceInterval": [
                                                                                                                                                          8,
                                                                                                                                                          7
                                                                                                                                                        ]
                                                                                                                                                      },
                                                                                                                                                      "children": {
                                                                                                                                                        "result": [],
                                                                                                                                                        "errors": []
                                                                                                                                                      }
                                                                                                                                                    },
                                                                                                                                                    {
                                                                                                                                                      "node": {
                                                                                                                                                        "parent": "FunctionName",
                                                                                                                                                        "text": "Count",
                                                                                                                                                        "sourceInterval": [
                                                                                                                                                          8,
                                                                                                                                                          8
                                                                                                                                                        ]
                                                                                                                                                      },
                                                                                                                                                      "children": {
                                                                                                                                                        "result": [
                                                                                                                                                          {
                                                                                                                                                            "node": {
                                                                                                                                                              "parent": "SymbolicName",
                                                                                                                                                              "text": "Count",
                                                                                                                                                              "sourceInterval": [
                                                                                                                                                                8,
                                                                                                                                                                8
                                                                                                                                                              ]
                                                                                                                                                            },
                                                                                                                                                            "children": {
                                                                                                                                                              "parent": "SymbolicName",
                                                                                                                                                              "text": "Count",
                                                                                                                                                              "sourceInterval": [
                                                                                                                                                                8,
                                                                                                                                                                8
                                                                                                                                                              ]
                                                                                                                                                            }
                                                                                                                                                          }
                                                                                                                                                        ],
                                                                                                                                                        "errors": []
                                                                                                                                                      }
                                                                                                                                                    }
                                                                                                                                                  ],
                                                                                                                                                  "errors": []
                                                                                                                                                }
                                                                                                                                              },
                                                                                                                                              {
                                                                                                                                                "node": {
                                                                                                                                                  "parent": "FunctionInvocation",
                                                                                                                                                  "text": "(",
                                                                                                                                                  "sourceInterval": [
                                                                                                                                                    9,
                                                                                                                                                    9
                                                                                                                                                  ]
                                                                                                                                                },
                                                                                                                                                "children": {
                                                                                                                                                  "parent": "FunctionInvocation",
                                                                                                                                                  "text": "(",
                                                                                                                                                  "sourceInterval": [
                                                                                                                                                    9,
                                                                                                                                                    9
                                                                                                                                                  ]
                                                                                                                                                }
                                                                                                                                              },
                                                                                                                                              {
                                                                                                                                                "node": {
                                                                                                                                                  "parent": "FunctionInvocation",
                                                                                                                                                  "text": "n",
                                                                                                                                                  "sourceInterval": [
                                                                                                                                                    10,
                                                                                                                                                    10
                                                                                                                                                  ]
                                                                                                                                                },
                                                                                                                                                "children": {
                                                                                                                                                  "result": [
                                                                                                                                                    {
                                                                                                                                                      "node": {
                                                                                                                                                        "parent": "Expression",
                                                                                                                                                        "text": "n",
                                                                                                                                                        "sourceInterval": [
                                                                                                                                                          10,
                                                                                                                                                          10
                                                                                                                                                        ]
                                                                                                                                                      },
                                                                                                                                                      "children": {
                                                                                                                                                        "result": [
                                                                                                                                                          {
                                                                                                                                                            "node": {
                                                                                                                                                              "parent": "OrExpression",
                                                                                                                                                              "text": "n",
                                                                                                                                                              "sourceInterval": [
                                                                                                                                                                10,
                                                                                                                                                                10
                                                                                                                                                              ]
                                                                                                                                                            },
                                                                                                                                                            "children": {
                                                                                                                                                              "result": [
                                                                                                                                                                {
                                                                                                                                                                  "node": {
                                                                                                                                                                    "parent": "XorExpression",
                                                                                                                                                                    "text": "n",
                                                                                                                                                                    "sourceInterval": [
                                                                                                                                                                      10,
                                                                                                                                                                      10
                                                                                                                                                                    ]
                                                                                                                                                                  },
                                                                                                                                                                  "children": {
                                                                                                                                                                    "result": [
                                                                                                                                                                      {
                                                                                                                                                                        "node": {
                                                                                                                                                                          "parent": "AndExpression",
                                                                                                                                                                          "text": "n",
                                                                                                                                                                          "sourceInterval": [
                                                                                                                                                                            10,
                                                                                                                                                                            10
                                                                                                                                                                          ]
                                                                                                                                                                        },
                                                                                                                                                                        "children": {
                                                                                                                                                                          "result": [
                                                                                                                                                                            {
                                                                                                                                                                              "node": {
                                                                                                                                                                                "parent": "NotExpression",
                                                                                                                                                                                "text": "n",
                                                                                                                                                                                "sourceInterval": [
                                                                                                                                                                                  10,
                                                                                                                                                                                  10
                                                                                                                                                                                ]
                                                                                                                                                                              },
                                                                                                                                                                              "children": {
                                                                                                                                                                                "result": [
                                                                                                                                                                                  {
                                                                                                                                                                                    "node": {
                                                                                                                                                                                      "parent": "ComparisonExpression",
                                                                                                                                                                                      "text": "n",
                                                                                                                                                                                      "sourceInterval": [
                                                                                                                                                                                        10,
                                                                                                                                                                                        10
                                                                                                                                                                                      ]
                                                                                                                                                                                    },
                                                                                                                                                                                    "children": {
                                                                                                                                                                                      "result": [
                                                                                                                                                                                        {
                                                                                                                                                                                          "node": {
                                                                                                                                                                                            "parent": "AddOrSubtractExpression",
                                                                                                                                                                                            "text": "n",
                                                                                                                                                                                            "sourceInterval": [
                                                                                                                                                                                              10,
                                                                                                                                                                                              10
                                                                                                                                                                                            ]
                                                                                                                                                                                          },
                                                                                                                                                                                          "children": {
                                                                                                                                                                                            "result": [
                                                                                                                                                                                              {
                                                                                                                                                                                                "node": {
                                                                                                                                                                                                  "parent": "MultiplyDivideModuloExpression",
                                                                                                                                                                                                  "text": "n",
                                                                                                                                                                                                  "sourceInterval": [
                                                                                                                                                                                                    10,
                                                                                                                                                                                                    10
                                                                                                                                                                                                  ]
                                                                                                                                                                                                },
                                                                                                                                                                                                "children": {
                                                                                                                                                                                                  "result": [
                                                                                                                                                                                                    {
                                                                                                                                                                                                      "node": {
                                                                                                                                                                                                        "parent": "PowerOfExpression",
                                                                                                                                                                                                        "text": "n",
                                                                                                                                                                                                        "sourceInterval": [
                                                                                                                                                                                                          10,
                                                                                                                                                                                                          10
                                                                                                                                                                                                        ]
                                                                                                                                                                                                      },
                                                                                                                                                                                                      "children": {
                                                                                                                                                                                                        "result": [
                                                                                                                                                                                                          {
                                                                                                                                                                                                            "node": {
                                                                                                                                                                                                              "parent": "UnaryAddOrSubtractExpression",
                                                                                                                                                                                                              "text": "n",
                                                                                                                                                                                                              "sourceInterval": [
                                                                                                                                                                                                                10,
                                                                                                                                                                                                                10
                                                                                                                                                                                                              ]
                                                                                                                                                                                                            },
                                                                                                                                                                                                            "children": {
                                                                                                                                                                                                              "result": [
                                                                                                                                                                                                                {
                                                                                                                                                                                                                  "node": {
                                                                                                                                                                                                                    "parent": "StringListNullOperatorExpression",
                                                                                                                                                                                                                    "text": "n",
                                                                                                                                                                                                                    "sourceInterval": [
                                                                                                                                                                                                                      10,
                                                                                                                                                                                                                      10
                                                                                                                                                                                                                    ]
                                                                                                                                                                                                                  },
                                                                                                                                                                                                                  "children": {
                                                                                                                                                                                                                    "result": [
                                                                                                                                                                                                                      {
                                                                                                                                                                                                                        "node": {
                                                                                                                                                                                                                          "parent": "PropertyOrLabelsExpression",
                                                                                                                                                                                                                          "text": "n",
                                                                                                                                                                                                                          "sourceInterval": [
                                                                                                                                                                                                                            10,
                                                                                                                                                                                                                            10
                                                                                                                                                                                                                          ]
                                                                                                                                                                                                                        },
                                                                                                                                                                                                                        "children": {
                                                                                                                                                                                                                          "result": [
                                                                                                                                                                                                                            {
                                                                                                                                                                                                                              "node": {
                                                                                                                                                                                                                                "parent": "Atom",
                                                                                                                                                                                                                                "text": "n",
                                                                                                                                                                                                                                "sourceInterval": [
                                                                                                                                                                                                                                  10,
                                                                                                                                                                                                                                  10
                                                                                                                                                                                                                                ]
                                                                                                                                                                                                                              },
                                                                                                                                                                                                                              "children": {
                                                                                                                                                                                                                                "result": [
                                                                                                                                                                                                                                  {
                                                                                                                                                                                                                                    "node": {
                                                                                                                                                                                                                                      "parent": "Variable",
                                                                                                                                                                                                                                      "text": "n",
                                                                                                                                                                                                                                      "sourceInterval": [
                                                                                                                                                                                                                                        10,
                                                                                                                                                                                                                                        10
                                                                                                                                                                                                                                      ]
                                                                                                                                                                                                                                    },
                                                                                                                                                                                                                                    "children": {
                                                                                                                                                                                                                                      "result": [
                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                          "node": {
                                                                                                                                                                                                                                            "parent": "SymbolicName",
                                                                                                                                                                                                                                            "text": "n",
                                                                                                                                                                                                                                            "sourceInterval": [
                                                                                                                                                                                                                                              10,
                                                                                                                                                                                                                                              10
                                                                                                                                                                                                                                            ]
                                                                                                                                                                                                                                          },
                                                                                                                                                                                                                                          "children": {
                                                                                                                                                                                                                                            "parent": "SymbolicName",
                                                                                                                                                                                                                                            "text": "n",
                                                                                                                                                                                                                                            "sourceInterval": [
                                                                                                                                                                                                                                              10,
                                                                                                                                                                                                                                              10
                                                                                                                                                                                                                                            ]
                                                                                                                                                                                                                                          }
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                      ],
                                                                                                                                                                                                                                      "errors": []
                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                  }
                                                                                                                                                                                                                                ],
                                                                                                                                                                                                                                "errors": []
                                                                                                                                                                                                                              }
                                                                                                                                                                                                                            }
                                                                                                                                                                                                                          ],
                                                                                                                                                                                                                          "errors": []
                                                                                                                                                                                                                        }
                                                                                                                                                                                                                      }
                                                                                                                                                                                                                    ],
                                                                                                                                                                                                                    "errors": []
                                                                                                                                                                                                                  }
                                                                                                                                                                                                                }
                                                                                                                                                                                                              ],
                                                                                                                                                                                                              "errors": []
                                                                                                                                                                                                            }
                                                                                                                                                                                                          }
                                                                                                                                                                                                        ],
                                                                                                                                                                                                        "errors": []
                                                                                                                                                                                                      }
                                                                                                                                                                                                    }
                                                                                                                                                                                                  ],
                                                                                                                                                                                                  "errors": []
                                                                                                                                                                                                }
                                                                                                                                                                                              }
                                                                                                                                                                                            ],
                                                                                                                                                                                            "errors": []
                                                                                                                                                                                          }
                                                                                                                                                                                        }
                                                                                                                                                                                      ],
                                                                                                                                                                                      "errors": []
                                                                                                                                                                                    }
                                                                                                                                                                                  }
                                                                                                                                                                                ],
                                                                                                                                                                                "errors": []
                                                                                                                                                                              }
                                                                                                                                                                            }
                                                                                                                                                                          ],
                                                                                                                                                                          "errors": []
                                                                                                                                                                        }
                                                                                                                                                                      }
                                                                                                                                                                    ],
                                                                                                                                                                    "errors": []
                                                                                                                                                                  }
                                                                                                                                                                }
                                                                                                                                                              ],
                                                                                                                                                              "errors": []
                                                                                                                                                            }
                                                                                                                                                          }
                                                                                                                                                        ],
                                                                                                                                                        "errors": []
                                                                                                                                                      }
                                                                                                                                                    }
                                                                                                                                                  ],
                                                                                                                                                  "errors": []
                                                                                                                                                }
                                                                                                                                              },
                                                                                                                                              {
                                                                                                                                                "node": {
                                                                                                                                                  "parent": "FunctionInvocation",
                                                                                                                                                  "text": ")",
                                                                                                                                                  "sourceInterval": [
                                                                                                                                                    11,
                                                                                                                                                    11
                                                                                                                                                  ]
                                                                                                                                                },
                                                                                                                                                "children": {
                                                                                                                                                  "parent": "FunctionInvocation",
                                                                                                                                                  "text": ")",
                                                                                                                                                  "sourceInterval": [
                                                                                                                                                    11,
                                                                                                                                                    11
                                                                                                                                                  ]
                                                                                                                                                }
                                                                                                                                              }
                                                                                                                                            ],
                                                                                                                                            "errors": []
                                                                                                                                          }
                                                                                                                                        }
                                                                                                                                      ],
                                                                                                                                      "errors": []
                                                                                                                                    }
                                                                                                                                  }
                                                                                                                                ],
                                                                                                                                "errors": []
                                                                                                                              }
                                                                                                                            }
                                                                                                                          ],
                                                                                                                          "errors": []
                                                                                                                        }
                                                                                                                      }
                                                                                                                    ],
                                                                                                                    "errors": []
                                                                                                                  }
                                                                                                                }
                                                                                                              ],
                                                                                                              "errors": []
                                                                                                            }
                                                                                                          }
                                                                                                        ],
                                                                                                        "errors": []
                                                                                                      }
                                                                                                    }
                                                                                                  ],
                                                                                                  "errors": []
                                                                                                }
                                                                                              }
                                                                                            ],
                                                                                            "errors": []
                                                                                          }
                                                                                        }
                                                                                      ],
                                                                                      "errors": []
                                                                                    }
                                                                                  }
                                                                                ],
                                                                                "errors": []
                                                                              }
                                                                            }
                                                                          ],
                                                                          "errors": []
                                                                        }
                                                                      }
                                                                    ],
                                                                    "errors": []
                                                                  }
                                                                }
                                                              ],
                                                              "errors": []
                                                            }
                                                          }
                                                        ],
                                                        "errors": []
                                                      }
                                                    }
                                                  ],
                                                  "errors": []
                                                }
                                              }
                                            ],
                                            "errors": []
                                          }
                                        }
                                      ],
                                      "errors": []
                                    }
                                  }
                                ],
                                "errors": []
                              }
                            }
                          ],
                          "errors": []
                        }
                      }
                    ],
                    "errors": []
                  }
                }
              ],
              "errors": []
            }
          }
        ],
        "errors": []
      }
    },
    {
      "node": {
        "parent": "Cypher",
        "text": ";",
        "sourceInterval": [
          12,
          12
        ]
      },
      "children": {
        "parent": "Cypher",
        "text": ";",
        "sourceInterval": [
          12,
          12
        ]
      }
    },
    {
      "node": {
        "parent": "Cypher",
        "text": "<EOF>",
        "sourceInterval": [
          13,
          13
        ]
      },
      "children": {
        "parent": "Cypher",
        "text": "<EOF>",
        "sourceInterval": [
          13,
          13
        ]
      }
    }
  ],
  "errors": []
}
```
