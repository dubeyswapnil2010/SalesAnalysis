# Excel Formulas Quick Reference

## 1. CALCULATION FORMULAS

### Revenue Calculation
```excel
=B2*C2
```
**Purpose:** Quantity × Price
**Location:** Column I (after importing data)
**Example:** =F2*G2 (Rows 2-35)

### Profit Margin %
```excel
=IF(I2=0,0,(H2/I2)*100)
```
**Purpose:** Calculate profit as percentage of revenue
**Safety:** IF statement prevents division by zero
**Format as:** Percentage (0 decimal places)

### Profit Amount
```excel
=I2-H2
```
**Purpose:** Revenue - Cost = Profit
**Alternative:** Use if profit column isn't pre-filled

---

## 2. LOOKUP FORMULAS

### VLOOKUP (Traditional)
```excel
=VLOOKUP("product_name", Table_Range, 3, FALSE)
```
**Parameters:**
- "product_name" = Search term (exact or use cell reference)
- Table_Range = Data to search in
- 3 = Return value from 3rd column
- FALSE = Exact match

**Example (Find product price):**
```excel
=VLOOKUP(D2, Products!$A$2:$C$100, 3, FALSE)
```

### XLOOKUP (Modern - Excel 365+)
```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])
```

**Advantages over VLOOKUP:**
- Search column can be anywhere (not just first)
- Search left or right
- Returns error message if not found

**Example:**
```excel
=XLOOKUP(D2, Products!$A:$A, Products!$C:$C, "Product Not Found")
```

---

## 3. CONDITIONAL FORMULAS

### Simple IF Statement
```excel
=IF(I2>500, "High Sales", "Low Sales")
```
**Purpose:** Classify sales into High/Low
**Use:** Create Column K for classification

### Nested IF (3-tier Classification)
```excel
=IF(I2>=1000, "Premium", IF(I2>=500, "Standard", "Economy"))
```
**Tiers:**
- ≥ $1000 = Premium
- $500-$999 = Standard
- < $500 = Economy

### IF with AND Conditions
```excel
=IF(AND(D2="North", I2>500), "High North Sales", "Other")
```
**Purpose:** Multiple conditions must be TRUE

### IF with OR Conditions
```excel
=IF(OR(D2="North", D2="South"), "Major Region", "Minor Region")
```
**Purpose:** Any condition being TRUE triggers result

---

## 4. AGGREGATION FORMULAS (SUMIFS, COUNTIFS)

### SUMIFS - Sum with Multiple Criteria
```excel
=SUMIFS(sum_range, criteria_range1, criterion1, criteria_range2, criterion2, ...)
```

**Example 1: Total Revenue for North Region**
```excel
=SUMIFS($I$2:$I$35, $D$2:$D$35, "North")
```

**Example 2: Total Revenue for North + Electronics**
```excel
=SUMIFS($I$2:$I$35, $D$2:$D$35, "North", $E$2:$E$35, "Electronics")
```

**Example 3: Revenue where quantity > 5**
```excel
=SUMIFS($I$2:$I$35, $F$2:$F$35, ">5")
```

**Example 4: Revenue with variable criteria (reference cell)**
```excel
=SUMIFS($I$2:$I$35, $D$2:$D$35, L2)
```
*Where L2 contains the region name*

### COUNTIFS - Count with Multiple Criteria
```excel
=COUNTIFS($D$2:$D$35, "North", $I$2:$I$35, ">1000")
```
**Purpose:** Count rows where region="North" AND Revenue>$1000

**Example: Count high-value orders by region**
```excel
=COUNTIFS($D$2:$D$35, "South", $I$2:$I$35, ">500")
```

### SUMPRODUCT - Complex Calculations
```excel
=SUMPRODUCT(($D$2:$D$35="North")*($E$2:$E$35="Electronics")*($I$2:$I$35))
```
**Purpose:** Sum revenue where region=North AND category=Electronics
**Advantage:** More flexible than SUMIFS for complex conditions

---

## 5. DASHBOARD KPI FORMULAS

### Total Sales
```excel
=SUM('Raw Data'!I:I)
```
**Alternative (specific range):**
```excel
=SUM('Raw Data'!I2:I35)
```

### Total Profit
```excel
=SUM('Raw Data'!H:H)
```

### Total Orders Count
```excel
=COUNTA('Raw Data'!A2:A35)
```
**Note:** Excludes header row

### Average Order Value
```excel
=AVERAGE('Raw Data'!I2:I35)
```

### Average Profit Margin %
```excel
=AVERAGE('Raw Data'!J2:J35)
```

### Orders > $500
```excel
=COUNTIF('Raw Data'!I2:I35, ">500")
```

---

## 6. TEXT FORMULAS

### Concatenate Text
```excel
=CONCATENATE(A2, " - ", D2)
```
*Creates: "O001 - North"*

**Or use & operator:**
```excel
=A2 & " - " & D2
```

### Extract Text from String
```excel
=MID(A2, 2, 3)
```
**Purpose:** Get characters 2-4 from order_id

### Convert to Uppercase/Lowercase
```excel
=UPPER(C2)        = "JOHN SMITH"
=LOWER(C2)        = "john smith"
=PROPER(C2)       = "John Smith"
```

---

## 7. DATE FORMULAS

### Current Date
```excel
=TODAY()
```

### Days Since Order
```excel
=TODAY()-B2
```

### Extract Month/Year
```excel
=MONTH(B2)        Returns: 1-12
=YEAR(B2)         Returns: 2024
```

### Format Date as Text
```excel
=TEXT(B2, "MMMM DD, YYYY")
```
*Returns: "January 05, 2024"*

---

## 8. PIVOT TABLE FORMULAS

### GETPIVOTDATA
Use to reference values from a pivot table:

```excel
=GETPIVOTDATA("Sum of Revenue", $A$3, "Region", "North")
```
**Purpose:** Retrieve specific value from pivot table

---

## 9. ERROR HANDLING

### IFERROR
```excel
=IFERROR(I2/H2, 0)
```
**Purpose:** If error occurs (e.g., division by zero), return 0

### IFNA
```excel
=IFNA(VLOOKUP(D2, Products!$A:$C, 3, FALSE), "Not Found")
```
**Purpose:** Handle #N/A errors from lookup functions

---

## FORMULA PLACEMENT GUIDE

| Formula | Cell Location | Purpose |
|---------|---|---|
| Revenue = Qty × Price | Column I | Calculate total order value |
| Profit % | Column J | Calculate margin percentage |
| High/Low Sales | Column K | Classify sales tier |
| KPI: Total Sales | Dashboard B2 | $21,360 |
| KPI: Total Profit | Dashboard D2 | $4,733 |
| KPI: Total Orders | Dashboard F2 | 32 |
| KPI: Avg Order | Dashboard H2 | $668 |
| Sales by Region | Reference Sheet | SUMIFS formulas |

---

## BEST PRACTICES

### Use Absolute References for Ranges
```excel
❌ Bad:  =SUM(I2:I35)
✓ Good: =SUM($I$2:$I$35)
```
Absolute references ($) don't change when copied

### Lock Headers in Formulas
```excel
✓ Good: =SUMIFS($I$2:$I$35, $D$2:$D$35, "North")
```
Prevents accidental range changes

### Use Named Ranges
Instead of: `=SUM(I2:I35)`
Use: `=SUM(Revenue)` (after naming range I2:I35 as "Revenue")

**To create named range:**
- Select range → Formulas → Define Name → Enter "Revenue"

### Document Complex Formulas
Add comments to complex calculations:
- Right-click cell → Insert Comment
- Explain what the formula does

---

## COMMON FORMULA ERRORS

| Error | Cause | Solution |
|-------|-------|----------|
| #N/A | Value not found in VLOOKUP | Check spelling, use FALSE for exact match |
| #DIV/0! | Division by zero | Use IF statement: =IF(B2=0,0,A2/B2) |
| #REF! | Deleted referenced cell | Restore deleted cell or update formula |
| #VALUE! | Wrong data type in formula | Ensure all references are numbers/text as needed |
| #NAME? | Typo in formula | Check formula spelling |

---

## PRACTICE EXERCISES

1. **Create a formula** that sums revenue only for "Electronics" category
   ```
   Answer: =SUMIF($E$2:$E$35, "Electronics", $I$2:$I$35)
   ```

2. **Create a formula** that counts orders > $1000 in the "West" region
   ```
   Answer: =COUNTIFS($D$2:$D$35, "West", $I$2:$I$35, ">1000")
   ```

3. **Create a formula** that shows "High" if profit is > $200, else "Low"
   ```
   Answer: =IF(H2>200, "High", "Low")
   ```

---

## Excel Keyboard Shortcuts for Formulas

| Action | Shortcut |
|--------|----------|
| Enter formula | Ctrl + Shift + Enter (for array formulas) |
| Edit formula | F2 |
| Open function wizard | Ctrl + A (after = sign) |
| Copy cell | Ctrl + C |
| Paste formula | Ctrl + V |
| Paste Special (values only) | Ctrl + Shift + V |
| Go to cell | Ctrl + G or F5 |
| Fill down | Ctrl + D |

---

**Ready to use these formulas in your Excel dashboard! Copy and paste them as needed.**
