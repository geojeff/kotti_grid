import colander

from kotti.views.slots import assign_slot

from kotti_settings.config import SlotSchemaNode
from kotti_settings.config import ShowInContextSchemaNode
from kotti_settings.util import add_settings
from kotti_settings.util import get_setting
from kotti_grid import _


class MarginXSchemaNode(colander.SchemaNode):
    name = 'margin_x'
    title = _(u'Margin X')
    default = 10


class MarginYSchemaNode(colander.SchemaNode):
    name = 'margin_y'
    title = _(u'Margin Y')
    default = 10


class DimensionXSchemaNode(colander.SchemaNode):
    name = 'dimension_x'
    title = _(u'Dimension X')
    default = 150


class DimensionYSchemaNode(colander.SchemaNode):
    name = 'dimension_y'
    title = _(u'Dimension Y')
    default = 150


class GridSchema(colander.MappingSchema):
    slot = SlotSchemaNode(colander.String())
    show_in_context = ShowInContextSchemaNode(colander.String())
    dimension_x = DimensionXSchemaNode(colander.Integer())
    dimension_y = DimensionYSchemaNode(colander.Integer())
    margin_x = MarginXSchemaNode(colander.Integer())
    margin_y = MarginYSchemaNode(colander.Integer())


GridSettings = {
    'name': 'grid_settings',
    'title': _(u'Grid Settings'),
    'description': _(u"Settings for kotti_grid"),
    'success_message': _(u"Successfully saved kotti_grid settings."),
    'schema_factory': GridSchema,
}


def populate():
    add_settings(GridSettings)
    slot = get_setting(u'slot', u'belowcontent')
    assign_slot('grid-widget', slot)
