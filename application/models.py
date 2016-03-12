from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def get_or_create(model, val):
    m = model.query.filter_by(name=val).first()
    if not m:
        m = model(val)
        db.session.add(m)
    return m


class Circulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    bookname = db.Column(db.String)
    url = db.Column(db.String)
    tag = db.Column(db.String)
    year = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    count = db.Column(db.Integer)

    def __init__(self, type, bookname, url, year, tag, rank, count):
        self.type = type
        self.bookname = bookname
        self.url = url
        self.tag = tag
        self.year = year
        self.rank = rank
        self.count = count


class Sheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    url = db.Column(db.String(255))

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department',
                                 backref=db.backref('sheets', lazy='dynamic'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    subject = db.relationship('Subject',
                              backref=db.backref('sheets', lazy='dynamic'))
    examtype_id = db.Column(db.Integer, db.ForeignKey('examtype.id'))
    examtype = db.relationship('Examtype',
                               backref=db.backref('sheets', lazy='dynamic'))

    def __init__(self, url, year, department, subject, examtype):
        self.url = url
        self.year = year
        self.department = department
        self.subject = subject
        self.examtype = examtype

    def __repr__(self):
        return '<Sheet %r>' % self.subject


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%r' % self.name


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%r' % self.name


class Examtype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%r' % self.name
