"""add content parts to message

Revision ID: 2cceb07c2384
Revises: 77de976590ae
Create Date: 2025-03-13 14:30:53.177061

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op
from letta.orm.custom_columns import MessageContentColumn

# revision identifiers, used by Alembic.
revision: str = "2cceb07c2384"
down_revision: Union[str, None] = "77de976590ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("messages", sa.Column("content", MessageContentColumn(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("messages", "content")
    # ### end Alembic commands ###
