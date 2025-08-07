TITLE = "Integral of a Rational Function with Square Roots"
MAIN_EQ = r"\int \frac{\sqrt{x+1} - \sqrt{x-1}}{\sqrt{x+1} + \sqrt{x-1}} \, dx"
STEPS = [
    r"\int \frac{(\sqrt{x+1} - \sqrt{x-1})^2}{(\sqrt{x+1})^2 - (\sqrt{x-1})^2} \, dx",
    r"\int \frac{(x+1) + (x-1) - 2\sqrt{(x+1)(x-1)}}{2} \, dx",
    r"\frac{1}{2} \int \left(2x - 2\sqrt{x^2 - 1}\right) \, dx",
    r"\int x \, dx - \int \sqrt{x^2 - 1} \, dx",
    r"\frac{x^2}{2} - \left( \frac{x}{2}\sqrt{x^2 - 1} - \frac{1}{2}\ln\left|x + \sqrt{x^2 - 1}\right| \right) + C"
]
FINAL_RESULT = r"\boxed{\frac{x^2}{2} - \frac{x}{2}\sqrt{x^2 - 1} + \frac{1}{2}\ln\left|x + \sqrt{x^2 - 1}\right| + C}"