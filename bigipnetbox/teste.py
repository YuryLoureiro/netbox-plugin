#Irule
class IruleListView(generic.ObjectListView):
    queryset = Irule.objects.all()
    table = IruleTable
    filterset = IruleFilterSet
    filterset_form = IruleFilterForm

class IruleView(generic.ObjectView):
    queryset = Irule.objects.all()
    table = IruleTable


class IruleEdit(generic.ObjectEditView):
    queryset = Irule.objects.all()
    form = IruleForm


class IruleDelete(generic.ObjectDeleteView):
    queryset = Irule.objects.all()


class IruleDeleteBulk(generic.BulkDeleteView):
    queryset = Irule.objects.all()
    table = IruleTable