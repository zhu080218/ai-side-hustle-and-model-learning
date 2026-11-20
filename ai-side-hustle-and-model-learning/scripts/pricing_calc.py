#!/usr/bin/env python3
"""AI 副业报价与有效时薪计算器。

两种用法：
  1) 已知报价，反算净收入与有效时薪
     python pricing_calc.py --quote 3000 --hours 12 --revisions 2 --revision-hours 1.5 --cost 200 --fee-rate 0.05
  2) 已知目标时薪，反推应报价格
     python pricing_calc.py --target-hourly 300 --hours 10 --cost 150 --fee-rate 0.1
"""
import argparse
import sys


def fmt(x: float) -> str:
    return f"{x:,.0f}" if abs(x) >= 100 else f"{x:,.1f}"


def main() -> int:
    ap = argparse.ArgumentParser(description="报价与有效时薪计算器")
    ap.add_argument("--quote", type=float, help="客户报价 / 合同金额（元）")
    ap.add_argument("--hours", type=float, required=True, help="基础投入工时（小时）")
    ap.add_argument("--revisions", type=int, default=0, help="修改轮次")
    ap.add_argument("--revision-hours", type=float, default=0.0, help="每轮修改耗时（小时）")
    ap.add_argument("--cost", type=float, default=0.0, help="直接成本：素材、API、外包（元）")
    ap.add_argument("--fee-rate", type=float, default=0.0, help="平台抽成比例，如 0.05 表示 5%")
    ap.add_argument("--tax-rate", type=float, default=0.0, help="税费比例，如 0.06 表示 6%")
    ap.add_argument("--target-hourly", type=float, help="目标有效时薪（元/小时），用于反推报价")
    args = ap.parse_args()

    if args.fee_rate + args.tax_rate >= 1:
        print("错误：平台抽成 + 税费合计必须小于 100%", file=sys.stderr)
        return 2
    if args.target_hourly is None and args.quote is None:
        print("错误：请至少提供 --quote 或 --target-hourly", file=sys.stderr)
        return 2

    total_hours = args.hours + args.revisions * args.revision_hours
    if total_hours <= 0:
        print("错误：总工时必须为正数", file=sys.stderr)
        return 2

    deduction_rate = args.fee_rate + args.tax_rate

    if args.quote is not None:
        gross = args.quote
        fee = gross * args.fee_rate
        tax = gross * args.tax_rate
        net = gross - fee - tax - args.cost
        hourly = net / total_hours

        print("=== 报价体检 ===")
        print(f"合同金额        {fmt(gross)} 元")
        print(f"平台抽成        {fmt(fee)} 元（{args.fee_rate:.1%}）")
        print(f"税费            {fmt(tax)} 元（{args.tax_rate:.1%}）")
        print(f"直接成本        {fmt(args.cost)} 元")
        print(f"净收入          {fmt(net)} 元")
        print(f"总工时          {fmt(total_hours)} 小时（基础 {fmt(args.hours)} + 修改 {fmt(total_hours - args.hours)}）")
        print(f"有效时薪        {fmt(hourly)} 元/小时")
        if args.revision_hours > 0 and args.revisions > 0:
            print(f"每多一轮修改    {fmt(hourly * args.revision_hours)} 元")
            print(f"再加 2 轮修改   时薪降至 {fmt(net / (total_hours + 2 * args.revision_hours))} 元/小时")
        if net <= 0:
            print("提示：净收入不为正，直接成本或抽成已吞掉全部报价。")
        if args.target_hourly is not None:
            gap = hourly - args.target_hourly
            verdict = "高于" if gap >= 0 else "低于"
            print(f"对比目标时薪    {verdict}目标 {fmt(abs(gap))} 元/小时")

    if args.target_hourly is not None:
        required = (args.target_hourly * total_hours + args.cost) / (1 - deduction_rate)
        print()
        print("=== 反推报价 ===")
        print(f"目标时薪        {fmt(args.target_hourly)} 元/小时 × {fmt(total_hours)} 小时")
        print(f"应报价格        {fmt(required)} 元（含成本与抽成）")
        print(f"建议报价区间    {fmt(required * 1.1)} – {fmt(required * 1.3)} 元（含 10%–30% 沟通与返工冗余）")

    return 0


if __name__ == "__main__":
    sys.exit(main())
