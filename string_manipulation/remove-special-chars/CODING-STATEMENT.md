# Remove non-alphanumeric chars from string beginning and end
# and count its appearances, case-insensitive

## Example 1

text = "lead cow baby success pink bigger green cake"

{
    "lead": 1,
    "cow": 1,
    "baby": 1,
    "success": 1,
    "pink": 1,
    "bigger": 1,
    "green": 1,
    "cake": 1,
}

## Example 2

text = "lead Cow baby success cow bigger green cake"

{
    "lead": 1,
    "cow": 2,
    "baby": 1,
    "success": 1,
    "bigger": 1,
    "green": 1,
    "cake": 1,
}

## Example 3

text = "lead Cow baby! success cow bigger $green cake"

{
    "lead": 1,
    "cow": 2,
    "baby": 1,
    "success": 1,
    "bigger": 1,
    "green": 1,
    "cake": 1,
}

## Example 4

text = "l3!!4d Cow baby! success cow b1,gg3r $gr33.n cake"

{
    "l3!!4d": 1,
    "cow": 2,
    "baby": 1,
    "success": 1,
    "b1,gg3r": 1,
    "gr33.n": 1,
    "cake": 1,
}

## Example 5

text = ""l3"4d""" Cow !!baby! succ..ess cow #b1,gg3,r $gr33.n# cake"

{
    "l3"4d": 1,
    "cow": 2,
    "baby": 1,
    "succ..ess": 1,
    "b1,gg3,r": 1,
    "gr33.n": 1,
    "cake": 1,
}
