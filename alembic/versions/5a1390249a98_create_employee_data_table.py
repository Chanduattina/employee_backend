"""create employee_data table

Revision ID: 5a1390249a98
Revises: 
Create Date: 2022-11-08 17:16:09.126412

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5a1390249a98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "employee",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('yob', sa.Integer)
    )


def downgrade():
    op.drop_table('employee')
