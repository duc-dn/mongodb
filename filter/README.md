### $filter
---
- Được dùng để filter các giá trị thỏa mãn trong array của 1 document bất kỳ, lấy ra các giá trị thỏa mãn trong mảng
---
```
{
   $filter:
      {
         input: <array>,
         cond: <expression>,
         as: <string>,
         limit: <number expression>
      }
}
```
---
