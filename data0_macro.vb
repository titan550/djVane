Sub Macro5()
'
' Macro5 Macro
'

'
Dim i As Integer
i = 1
While i <= 50

    Columns(i + 1).Select
    Selection.Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove
    Columns(i).Select
    Selection.TextToColumns Destination:=Cells(1, i), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=False, _
        Semicolon:=False, Comma:=True, Space:=False, Other:=False, FieldInfo _
        :=Array(Array(1, 1), Array(2, 1))
i = i + 2
Wend
End Sub