"""bulckinsert data

Revision ID: c30e357544ba
Revises: 5a1390249a98
Create Date: 2022-11-09 17:36:20.889357

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column, Integer, String

# revision identifiers, used by Alembic.
revision = 'c30e357544ba'
down_revision = '5a1390249a98'
branch_labels = None
depends_on = None


def upgrade() -> None:
    emp_table = table('employee',
                      column('id', Integer),
                      column('name', String),
                      column('yob', Integer)
                      )

    op.bulk_insert(emp_table,
                   [
                       {'id': 1, 'name': 'chandu', "yob": 2000},
                       {'id': 2, 'name': 'ravin', "yob": 1982},
                       {'id': 3, 'name': 'geetha', "yob": 2002}
                   ]
                   )


def downgrade() -> None:
    pass
