"""Add new constraint for TimeSpent

Revision ID: 16328eae4b5f
Revises: 17ef8f7be758
Create Date: 2024-03-06 05:14:09.534846

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from zou.migrations.utils.base import BaseMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = "16328eae4b5f"
down_revision = "17ef8f7be758"
branch_labels = None
depends_on = None

base = declarative_base()


class TimeSpent(base, BaseMixin):
    """
    Describes the time spent by someone on a task.
    """

    __tablename__ = "time_spent"

    duration = sa.Column(sa.Float, nullable=False)
    date = sa.Column(sa.Date, nullable=False)

    task_id = sa.Column(
        UUIDType(binary=False), sa.ForeignKey("task.id"), index=True
    )
    person_id = sa.Column(
        UUIDType(binary=False), sa.ForeignKey("person.id"), index=True
    )

    __table_args__ = (
        sa.UniqueConstraint(
            "person_id", "task_id", "date", name="time_spent_uc"
        ),
    )


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table("time_spent", schema=None) as batch_op:
        session = Session(bind=op.get_bind())
        session.query(TimeSpent).where(TimeSpent.duration <= 0).delete()
        session.commit()
        batch_op.create_check_constraint(
            "check_duration_positive", "duration > 0"
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("time_spent", schema=None) as batch_op:
        batch_op.drop_constraint("check_duration_positive", type_="check")

    # ### end Alembic commands ###
